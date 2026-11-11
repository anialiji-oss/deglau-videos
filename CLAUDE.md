# Deglau Gaming – TikTok-Videos

Dieses Repo gehört Deglau (TikTok @deglaugaming). Ziel: Auf „Mach das Game X“ ein fertiges TikTok im Deglau-Stil bauen.

**Vor jeder Arbeit lesen:** `STIL.md` (alle Regeln, die Deglau festgelegt hat) und `referenz/voiceover-beispiele.md` (echte Scripts als Vorlage für Ton und Aufbau).

## Ablauf bei „Mach das Game X“ (festgelegt von Deglau)
Deglau spricht den Text **selbst** ein – kein Stimm-Klon (klingt nicht nach ihm).

**Schritt 1 – Claude:** Spiel recherchieren (Steam-Seite, neuester Trailer ansehen) und **Script schreiben** in Deglaus Stil
(Hook → Features → „Ich bin Deglau …“ → Features → Outro, Deutsch, locker, „ihr/du und deine Freunde“, ca. 25–40 s gesprochen).
Features nur so, wie sie im Trailer auch zu sehen sind, damit Bild und Text später passen. Dazu einen Vorschlag für die Titel-Box.
→ Script an Deglau schicken, auf Änderungswünsche warten.

**Schritt 2 – Deglau:** nimmt das Script auf und schickt die Aufnahme (Audio oder Video).

**Schritt 3 – Claude:** alles auf seine Aufnahme schneiden:
- Wort-Zeitstempel aus der Aufnahme (`scripts/words.py`), Namen/Begriffe korrigieren
- Neuesten Trailer holen (Steam-API, siehe STIL.md), Szenen passend zum Gesagten
- Intro: Hintergrundmusik → `tension.mp3` → Blitz + Beat am Ende des Hook-Satzes
- Logo, Titel-Box, Wort-für-Wort-Untertitel, große Wort-Effekte an coolen Stellen, Einblendungen
- Soundeffekte: **nur Steam (Sound + drehendes Logo)**. Alle anderen SFX macht Deglau selbst in CapCut (STIL.md, Abschnitt ⭐⭐ Aufgabenteilung)
- Übergänge (Blitz/Zoom-Punch) mitten im Video erlaubt, wenn es gut passt
- Export 1080x1920, 30 fps → an Deglau schicken

ElevenLabs („mainaccount“, `assets/stimme.json`) nur noch als Notlösung, wenn Deglau das ausdrücklich will.

## Dateien
- `assets/logo.png` – Logo freigestellt · `assets/caption.ttf` – Untertitel-Schrift (Montserrat Black Italic)
- `assets/musik/hintergrund_musik.mp3` – Intro-Musik · `assets/musik/mainbeat.mp3` – Beat, **Drop bei 13,77 s**
- `scripts/render.py` – **Haupt-Renderer**: `python3 scripts/render.py videos/<spiel>/edit.json` (Segmente, Intro/Blitz/Beat, Logo, Titel, Untertitel, große Wörter, SFX, Lautstärken)
- `scripts/words.py` – Wort-Zeitstempel (faster-whisper; `pip install faster-whisper`) · `scripts/render_test.py` – alter Test
- `videos/<spiel>/` – script.md, edit.json (Schnittplan), voice.m4a, words.json. Trailer liegen NICHT im Repo → neu laden (Steam-API) und Pfade in `sources` anpassen. Fertige MP4s werden nicht eingecheckt.
- edit.json-Segmente: `"fit": 1.35` = ganzes 16:9-Bild mit unscharfem Hintergrund; `cx` = horizontaler Ausschnitt 0–1; `"rect": [x,y,w,h]` (Anteile) = Ausschnitt vorab, z. B. eingebrannte Trailer-Texte/Untertitel unten wegschneiden `[0,0,1,0.78]`; `"wide"` = Zoom-Stufe (Standard 1.5)
- `"icons"`: kurze Bild-Einblendungen (drehendes Steam-Logo `spin: 1`, Spiel-Kachel `spin: 0`, Breite `size`, Höhe automatisch). Spiel-Kachel = Steam `header_image` mit runden Ecken (siehe videos/gold-mining-simulator-de/spiel_kachel.png)

## Offen
- Effekt „Wörter hinter der Figur“ technisch einrichten (Segmentierung)
