param([string]$Pptx,[string]$Pdf)
$pp = New-Object -ComObject PowerPoint.Application
try { $p = $pp.Presentations.Open($Pptx, $true, $false, $false); $p.SaveAs($Pdf, 32); $p.Close() }
finally { $pp.Quit(); [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pp) | Out-Null }
