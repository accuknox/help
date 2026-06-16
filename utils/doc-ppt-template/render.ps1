param(
  [string]$Pptx = "D:\Atharva\AccuKnox\HelpDocs\utils\ppt-output\<replace-with-output-filename>.pptx",
  [string]$Out  = "D:\Atharva\AccuKnox\HelpDocs\utils\ppt-output\render"
)
New-Item -ItemType Directory -Force -Path $Out | Out-Null
Get-ChildItem -Path $Out -Filter *.png -ErrorAction SilentlyContinue | Remove-Item -Force
$pp = New-Object -ComObject PowerPoint.Application
try {
  $pres = $pp.Presentations.Open($Pptx, $true, $false, $false)
  $n = $pres.Slides.Count
  for ($i=1; $i -le $n; $i++) {
    $f = Join-Path $Out ("slide-{0:D2}.png" -f $i)
    $pres.Slides.Item($i).Export($f, "PNG", 1280, 720)
  }
  Write-Output "Exported $n slides to $Out"
  $pres.Close()
} finally {
  $pp.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pp) | Out-Null
}
