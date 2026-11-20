# Deglau – GTA-6-Clips auf YouTube suchen und kurze Ausschnitte laden (läuft auf deinem PC)
#
# Einmalig installieren (PowerShell):
#   winget install yt-dlp.yt-dlp
#   winget install Gyan.FFmpeg
#
# 1) SUCHEN – schreibt alle Treffer in treffer.csv (Titel, Kanal, Link, Länge, Datum):
#   powershell -ExecutionPolicy Bypass -File clips_suchen.ps1
#   powershell -ExecutionPolicy Bypass -File clips_suchen.ps1 -Suche "GTA 6 red hulk","GTA 6 secret weapon"
#
# 2) LADEN – nur ein kurzes Stück aus einem Video (z. B. 1:05 bis 1:20):
#   powershell -ExecutionPolicy Bypass -File clips_suchen.ps1 -Link "https://www.youtube.com/watch?v=XXXX" -Von 1:05 -Bis 1:20 -Name waffe_boot
#
# Jeder geladene Clip wird mit Link + Kanal in quellen.txt eingetragen -> Creator im Post nennen.

param(
    [string[]]$Suche = @(
        "GTA 6 hidden weapons locations",
        "GTA 6 secret weapon",
        "GTA 6 best weapon free",
        "GTA 6 fastest car",
        "GTA 6 best car upgrade",
        "GTA 6 red hulk easter egg"
    ),
    [int]$ProSuche = 15,            # Treffer pro Suchbegriff
    [int]$MaxMinuten = 20,          # längere Videos (Streams) überspringen
    [string]$AbDatum = "20261119",  # nur Videos ab Release (JJJJMMTT)
    [string]$Link, [string]$Von, [string]$Bis, [string]$Name = "clip",
    [string]$Ordner = "$env:USERPROFILE\Deglau-clips\gta6"
)

New-Item -ItemType Directory -Force -Path $Ordner | Out-Null

if ($Link) {
    if (-not $Von -or -not $Bis) { Write-Host "Bitte -Von und -Bis angeben, z. B. -Von 1:05 -Bis 1:20"; exit 1 }
    $ziel = Join-Path $Ordner "$Name.mp4"
    yt-dlp -f "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]" --merge-output-format mp4 `
        --download-sections "*$Von-$Bis" --force-keyframes-at-cuts -o $ziel $Link
    $kanal = yt-dlp --print "%(channel)s" --skip-download $Link
    Add-Content -Path (Join-Path $Ordner "quellen.txt") -Value "$Name.mp4 | $Von-$Bis | $kanal | $Link"
    Write-Host "Fertig: $ziel"
    exit 0
}

$alle = @()
foreach ($s in $Suche) {
    Write-Host "Suche: $s"
    $zeilen = yt-dlp "ytsearchdate$($ProSuche):$s" --skip-download --no-warnings `
        --print "%(title)s`t%(channel)s`t%(webpage_url)s`t%(duration)s`t%(upload_date)s"
    foreach ($z in $zeilen) {
        $t = $z -split "`t"
        if ($t.Count -lt 5) { continue }
        $dauer = 0; [int]::TryParse($t[3], [ref]$dauer) | Out-Null
        if ($dauer -gt $MaxMinuten * 60) { continue }
        if ($t[4] -ne "NA" -and $t[4] -lt $AbDatum) { continue }
        $alle += [pscustomobject]@{
            Suche = $s; Titel = $t[0]; Kanal = $t[1]; Link = $t[2]
            Laenge = "{0}:{1:D2}" -f [math]::Floor($dauer / 60), ($dauer % 60); Datum = $t[4]
        }
    }
}
$alle = $alle | Sort-Object Link -Unique | Sort-Object Suche, Datum -Descending
$csv = Join-Path $Ordner "treffer.csv"
$alle | Export-Csv -Path $csv -NoTypeInformation -Encoding UTF8 -Delimiter ";"
$alle | Format-Table Suche, Laenge, Datum, Kanal, Titel -AutoSize
Write-Host "`n$($alle.Count) Treffer gespeichert in $csv"
Write-Host "Schau dir die Videos an, notier die guten Stellen (Minute) und lade sie mit -Link -Von -Bis -Name."
