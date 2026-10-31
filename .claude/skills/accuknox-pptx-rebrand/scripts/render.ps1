# Render a .pptx to PNGs with PowerPoint COM. Usage: render.ps1 <pptx> <outdir> [width] [slides like 1,2,5]
param([string]$Pptx, [string]$Out, [int]$Width = 1280, [string]$Slides = "")
$Pptx = (Resolve-Path $Pptx).Path
New-Item -ItemType Directory -Force $Out | Out-Null
$Out = (Resolve-Path $Out).Path
# Per-user Inter files do not reach Office until AddFontResource runs, so renders fall back to Calibri.
Add-Type -Namespace W -Name G -MemberDefinition '[DllImport("gdi32.dll", CharSet=CharSet.Unicode)] public static extern int AddFontResourceW(string f); [DllImport("user32.dll")] public static extern int SendMessageTimeoutW(IntPtr h, uint m, IntPtr w, IntPtr l, uint f, uint t, out IntPtr r);'
Get-ChildItem "$env:LOCALAPPDATA\Microsoft\Windows\Fonts\Inter*.ttf", "D:\AccuKnox\doc-ppt-template\assets\fonts\Inter*.ttf" -ErrorAction SilentlyContinue | ForEach-Object { [void][W.G]::AddFontResourceW($_.FullName) }
$r = [IntPtr]::Zero; [void][W.G]::SendMessageTimeoutW([IntPtr]0xffff, 0x1D, [IntPtr]::Zero, [IntPtr]::Zero, 2, 1000, [ref]$r)
if (Get-Process POWERPNT -ErrorAction SilentlyContinue) { Write-Warning "PowerPoint is already open. If renders show Calibri, close it and render again." }
# One render at a time: several builders share one PowerPoint, and Quit() would close another's file.
$lock = New-Object System.Threading.Mutex($false, "Global\AkPptxRender")
[void]$lock.WaitOne(600000)
$app = New-Object -ComObject PowerPoint.Application
try {
  $p = $app.Presentations.Open($Pptx, $true, $false, $false)
  $h = [int]($Width * $p.PageSetup.SlideHeight / $p.PageSetup.SlideWidth)
  $want = @()
  if ($Slides) { $want = $Slides.Split(",") | ForEach-Object { [int]$_ } }
  foreach ($s in $p.Slides) {
    if ($want.Count -and -not ($want -contains $s.SlideIndex)) { continue }
    $f = Join-Path $Out ("s{0:D2}.png" -f $s.SlideIndex)
    $s.Export($f, "PNG", $Width, $h)
  }
  Write-Output ("rendered {0} slides to {1}" -f $p.Slides.Count, $Out)
  $p.Close()
} finally { $app.Quit() | Out-Null; $lock.ReleaseMutex() }
