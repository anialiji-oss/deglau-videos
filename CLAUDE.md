# Deglau Gaming – TikTok-Videos

Dieses Repo gehört Deglau (TikTok @deglaugaming). Ziel: Auf „Mach das Game X“ ein fertiges TikTok im Deglau-Stil bauen.

**Vor jeder Arbeit lesen:** `STIL.md` (alle Regeln, die Deglau festgelegt hat) und `referenz/voiceover-beispiele.md` (echte Scripts als Vorlage für Ton und Aufbau).

## Ablauf bei „Mach das Game X“
1. Script in Deglaus Stil schreiben (Hook → Features → „Ich bin Deglau …“ → Features → Outro). Sprache: Deutsch, locker, „ihr/du und deine Freunde“.
2. Neuesten Trailer selbst holen (Steam-API, siehe STIL.md), bei Bedarf ältere Trailer ergänzen.
3. Voiceover mit Deglaus Stimme (Stimm-Klon – noch einzurichten).
4. Szenen passend zum Gesagten auswählen, Intro (Hintergrundmusik → Spannung → Blitz + Beat am Ende des Hooks), Logo, Titel-Box, Wort-für-Wort-Untertitel, Einblendungen, Soundeffekte.
5. Export 1080x1920, 30 fps.

## Dateien
- `assets/logo.png` – Logo freigestellt · `assets/caption.ttf` – Untertitel-Schrift (Montserrat Black Italic)
- `assets/musik/hintergrund_musik.mp3` – Intro-Musik · `assets/musik/mainbeat.mp3` – Beat, **Drop bei 13,77 s**
- `scripts/render_test.py` – Renderer (Intro/Blitz/Beat/Logo/Titel/Untertitel) · `scripts/words.py` – Wort-Zeitstempel (faster-whisper)

## Offen
- Saubere Stimmprobe + Entscheidung ElevenLabs vs. Open Source
- SFX: 10 Sounds von Deglau sind da (Meme + Klick/Pop/Tür); Whoosh, Hit, Boom noch selbst besorgen (CC0)
- Effekt „Wörter hinter der Figur“ technisch einrichten (Segmentierung)
