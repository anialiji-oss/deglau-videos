# Deglau Gaming – Videostil (analysiert aus 4 Videos)

## Format
- Hochformat 9:16 (Export 1080x1920, 30 fps), Länge ca. 26–60 s
- Voiceover läuft 26–40 s, danach nur noch Gameplay + Musik bis zum Ende

## Overlays
- **Logo**: gelber Kreis mit „D“ + Controller, oben mittig, die ganze Zeit sichtbar
- **Titel-Box**: weiße Box, schwarzer Text, 2 Zeilen + 🎮🔥, direkt unter dem Logo, nur in den ersten ca. 3–5 s
  - Beispiele: „The Wolf of Wall Street nur in einem Spiel“, „Betrunken Fußball spielen mit deinen Freunden“,
    „Als Schiri die ganze Matches kontrollieren“, „Das perfekt Spiel für Leute aus Polen“
- **Untertitel**: immer nur EIN Wort, GROSSBUCHSTABEN, weiß, fett und kursiv, schwarzer Rand, etwas unter der Bildmitte
- **Einblendungen**: Bild-im-Bild, sobald etwas Bestimmtes genannt wird (Filmszene bei „Leonardo DiCaprio“/„Jonah“,
  Handy-Feed bei „Insta oder Twitter“, Logo/Packshot beim Spielnamen)

## Schnitt
- Ein Schnitt alle 1–2 s, passend zu dem, was gerade gesagt wird
- Gameplay aus der Ich-Perspektive, Szenen passen wörtlich zum Text

## Script-Formel
1. **Hook (0–5 s)**: „In diesem Spiel …“ / „So ein … habt ihr bestimmt noch nie gespielt …“ – meist mit „du und deine Freunde“
2. **2–3 Features**, übertrieben und witzig („… ist es eh scheißegal“, „ballert ihr euch noch ein Bier“)
3. **Mitte (ca. 15–20 s)**: „Ich bin Deglau und stelle euch jeden Tag neue Spiele vor, also folgt mir doch gerne, um keine mehr zu verpassen.“
   - oft dazu: „markiert eure Freunde …“ oder eine Frage für die Kommentare („Ronaldo oder Messi?“)
4. **1–2 weitere Features**
5. **Outro**: „Das Spiel heißt ___, kommt für PC/PlayStation (raus), also verpasst es nicht, markiert eure Freunde – und jetzt viel Spaß euch.“

## Neu gewünscht (bisher in keinem der Videos)
- Intro: SpongeBob-Musik → Spannung steigt → Kamera-Blitz (weißer Flash + Auslöser-Geräusch) → Wechsel auf einen Beat

## Feste Regeln (von Deglau festgelegt)

### Intro / Musik
- Deglau redet **ab Sekunde 0 durchgehend**, nie erst nur Musik.
- Darunter: **Hintergrundmusik** (`hintergrund_musik.mp4`) → **Spannung steigt** während des Hook-Satzes
  (Übergang in den Aufbau vom Main Beat + `assets/sfx/tension.mp3`, Bild zoomt/wackelt/wird dunkler)
  → **Kamera-Blitz + Beat-Wechsel genau am Ende des Hook-Satzes** → **Main Beat** (`mainbeat.mp4`, Drop bei 13,77 s) leiser unter der Stimme.
- Titel-Box verschwindet mit dem Blitz.

### Gameplay-Material
- Den **Trailer immer selbst raussuchen**: immer den **neuesten Trailer** des Spiels
  (Quelle: Steam, `store.steampowered.com/api/storesearch` → `appdetails` → `movies`, neuester zuerst, HLS-Download funktioniert).
- Reicht der neueste Trailer nicht (z. B. viele Texttafeln), ältere Trailer / Gameplay-Videos des Spiels ergänzen.
- 16:9 → 9:16 mit **Zoom-Stufe 1.5** (Deglau): 1,5× breiterer Ausschnitt als Vollbild, unscharfer Rand oben/unten – sonst wirkt es zu nah. Im Renderer Standard (`wide`, pro Segment änderbar).
- Texttafeln/Logos/Endbilder des Trailers NICHT verwenden (nur Gameplay).

### Bild muss zum Gesagten passen
- Jede Szene muss zu dem passen, was gerade gesagt wird – wörtlich, wo möglich
  (sagt er „er schießt ein Tor“ → im Clip fällt ein Tor; „Bier“ → Bier im Bild; „Skins“ → Charakterauswahl).
- **NUR GAMEPLAY** (Deglau): keine Logos, Titelbilder, Texttafeln oder Endbilder aus dem Trailer („Carry On Together“-Logo, „Demo now available“ usw.) – auch nicht beim Spielnamen. Den Spielnamen zeigen wir mit unseren eigenen großen Wörtern über Gameplay.
- Ablauf: Schnitte im Trailer erkennen → Standbilder mit Zeitstempel ansehen → jedem Satz/Stichwort die passendste Stelle zuordnen.

### Soundeffekte – „Kirsche auf der Sahnetorte“ (gelernt aus Referenzvideo Download_12, Once Human)
Musik läuft durchgehend leise drunter, Stimme vorne. Dazu viele kurze, leise SFX, die nie ablenken, nur Details verstärken:
- ~~Whoosh vor jedem harten Schnitt~~ → **gestrichen (Deglau): kein Rauschen bei Schnitten.** Schnitte bleiben ohne Sound; Deglaus `swoosh.mp3` nur für Dinge, die wirklich fliegen (Wurf, reinfallende Wörter).
- **Pop/Klick pro Wort bei großen Text-Einblendungen**: „NEW“ – „MAPS“ – „AND“ – „EXPANSIONS“ (2,75–3,1 s) erscheinen Wort für Wort, jedes Wort mit eigenem Pop.
- **Bau-/Platzier-Geräusch („Thunk“, tief + kurz)**, genau in dem Frame, in dem ein Teil im Spiel erscheint
  (Floß wird gebaut: 10,2 s / 10,8 s / 11,2 s).
- **Action-Sounds passend zum Bild**: Kanone/Artillerie → Schuss, Monster/Leuchtturm „jagt dich“ → tiefes Dröhnen (28,3 s).
- **Logo-/Titel-Moment**: kräftiger Hit beim Spiel-Logo (34,1 s) und beim Code-Text (42,3 s).
- **Tiefer Boom/Bass-Hit am Ende** beim Endbild (44,7 s).
- Lautstärke: SFX deutlich leiser als die Stimme, eher Gefühl als Geräusch; nie über ein wichtiges Wort legen.

Regel für jedes Video: Bei jedem Schnitt, jeder Text-Einblendung und jeder sichtbaren Aktion im Gameplay (platzieren, schießen, Tor, hinfallen, kaufen …) prüfen, ob ein passender kleiner SFX drauf gehört.

### Große Wörter mit Effekt (Referenz: Once-Human-Video, Download_12)
Nur an **coolen Stellen** (Feature-Highlight, Spielname, Logo), nicht ständig. Nie einfach nur einblenden, die Wörter kommen **geschwungen** rein:
- **Reinfliegen mit Bewegungsunschärfe**: Wort schießt seitlich rein (Motion Blur), schwingt leicht über das Ziel hinaus und rastet ein
  (z. B. „EXPANSIONS“ rot, 3,1 s).
- **Reinfallen mit Federn**: Wort fällt von oben rein, wippt kurz nach und bleibt stehen („MOBILE“ grün, 13,7–14,0 s),
  die zweite Zeile kommt kleiner hinterher („SEA FORTRESS“ weiß, 14,2 s).
- **Wort für Wort aufbauen**: „NEW“ → „MAPS“ → „AND“ → „EXPANSIONS“, jedes Wort einzeln, jedes mit eigenem Whoosh/Pop.
- **Wörter HINTER der Figur**: Der Text steht im Bild-Hintergrund, die Figur/das Objekt läuft davor
  (Spiel-Logo „ONCE HUMAN“ fliegt von unten groß und glitchig rein und landet hinter dem Charakter, 34,1–34,5 s).
  Technik: Figur pro Frame freistellen (Segmentierung, z. B. rembg), Ebenen: Hintergrund → Text → Figur.
- Farben: Signalfarben mit dicker Schrift (grün/weiß/rot), ein Schlüsselwort farbig, der Rest weiß.
- Jeder dieser Effekte bekommt einen passenden **Whoosh/Swoosh** (Reinfliegen) bzw. **Hit** (Einrasten).
- Die normalen Wort-für-Wort-Untertitel bleiben trotzdem; während eines großen Wort-Effekts können sie kurz ausgeblendet werden.

### Soundeffekte – Beschaffung
- Grundstock: Deglaus eigene SFX (werden in `assets/sfx/` abgelegt).
- Passt keiner davon zur Stelle → **selbst einen passenden suchen und holen** (lizenzfrei, z. B. CC0) und ebenfalls in `assets/sfx/` speichern,
  damit er beim nächsten Mal da ist. Nur wenn nichts zu finden ist, selbst erzeugen.

### Deglaus SFX (`assets/sfx/`, Original-Lautstärke, nur Stille am Anfang entfernt)
Meme-/Comedy-Sounds (discord, error, fahhh, fart, alarm, scream) für lustige Momente; Klick-/Pop-/Tür-Sounds als kleine Detail-Effekte:
| Datei | Länge | Wofür |
|---|---|---|
| `discord_notification.mp3` | 0,5 s | Nachricht/Handy/Einblendung poppt auf, „Pling“-Moment |
| `error.mp3` | 1,0 s | etwas geht schief, falsche Entscheidung, Fail |
| `fahhh.mp3` | 2,0 s | ⛔ NICHT benutzen (Deglau: passt nicht) |
| `fart.mp3` | 0,4 s | peinlicher/dummer Moment, Pointe nach einem Witz |
| `alarm.mp3` | 0,7 s | Polizei, Gefahr, „Achtung“, etwas Verbotenes |
| `mouse_click.mp3` | 0,3 s | Klick: Menü, Kaufen, Auswählen, Button drücken, Handy antippen |
| `plop.mp3` | 0,3 s | Pop: Wort/Bild/Sticker erscheint, Text-Einblendung Wort für Wort |
| `minecraft_click.mp3` | 0,3 s | ⛔ NICHT benutzen (Deglau: passt nicht) |
| `minecraft_door_open.mp3` | 0,4 s | ⛔ NICHT benutzen (Deglau: passt nicht) |
| `minecraft_door_close.mp3` | 0,4 s | ⛔ NICHT benutzen (Deglau: passt nicht) |
| `swoosh.mp3` | 0,4 s | Whoosh: harter Schnitt, reinfliegende/reinschwingende Wörter, Bild-im-Bild fliegt rein (Peak sofort am Anfang → auf den Moment setzen) |
| `steam_sound.mp3` | 0,8 s | Steam-Sound: wenn Steam/PC/Release/„kommt auf Steam raus“ gesagt wird, Outro beim Spielnamen |
| `steam_achievement.mp3` | 0,8 s | Steam-Erfolg: etwas geschafft, Tor, Sieg, Level-Up, krasses Feature freigeschaltet (Höhepunkt am Ende bei 0,7 s → 0,7 s vor dem Moment starten) |
| `scream.mp3` | 1,8 s | Schrei: Horror, Monster, Absturz, jemand fliegt durch die Luft – Meme-Sound, sparsam |
| `tension.mp3` | 2,7 s | Spannungsaufbau fürs Intro: läuft während des Hook-Satzes, **Höhepunkt bei 1,9 s** → so legen, dass er genau auf Blitz + Beat-Wechsel landet (Start = Blitz − 1,9 s) |
- Meme-Sounds sparsam: höchstens 2–3 pro Video, auf die Pointe – nie über ein wichtiges Wort.
- Klick/Pop/Tür dürfen öfter kommen (Detail-Ebene), leise unter der Stimme.
- Fehlen noch: Hit (Einrasten eines Worts, Logo), Boom/Bass-Hit (Endbild) → selbst suchen (CC0) und hier ablegen.

### Aufnahme von Deglau (Tipps, die ihm mitgegeben werden)
- Handy nah am Mund, ruhiger Raum, **keine Musik** im Hintergrund – Musik und SFX kommen beim Schnitt dazu.
- Am Stück durchsprechen, im normalen TikTok-Tempo; Versprecher einfach den Satz nochmal sagen – Claude schneidet die beste Version raus.
- Format egal (Sprachmemo, MP3, Video).

### Lautstärken (Deglaus CapCut-Werte – fest)
Werte sind Verstärkung relativ zur **Original-Datei** (wie der Lautstärke-Regler in CapCut):
| Spur | Lautstärke |
|---|---|
| Stimme (Deglaus Aufnahme) | 0 dB (Original) |
| Hintergrundmusik (`assets/musik/hintergrund_musik.mp3`) | **−2,5 dB** |
| Main Beat (`assets/musik/mainbeat.mp3`) | **−13 dB** |
| Jeder Soundeffekt (`assets/sfx/*`) | **ca. −3 dB** |
- Deshalb SFX-Dateien **nie normalisieren**, nur Stille abschneiden – sonst stimmen die −3 dB nicht mehr.
- Abweichen nur, wenn ein Sound im Mix eindeutig untergeht oder ein wichtiges Wort zudeckt – dann in kleinen Schritten.

### Feedback Video 1 (Carry On Together)
- Deglau: „Die Soundeffekte passen gar nicht zusammen.“ → fahhh und alle Minecraft-Sounds raus. SFX lieber **weniger und einheitlicher** (swoosh, plop, mouse_click, steam_*, error) statt bunter Meme-Mix.
- Kein Logo/Titelbild aus dem Trailer – nur Gameplay.

### Eigene Sound-Auswahl (Mixkit, kostenlos auch kommerziell, ohne Namensnennung) – `assets/sfx/`
Stil wie im Once-Human-Video: dezent, „cinematic“, passt zusammen. **Peak-Zeiten stehen in `assets/sfx/_meta.json`** –
im Schnittplan gibt man an, wann der Sound am lautesten sein soll, der Renderer legt ihn automatisch richtig.
| Datei | Wofür |
|---|---|
| `whoosh_quick`, `whoosh_air`, `whoosh_soft` | ⛔ NICHT benutzen – Deglau: „unnötiges Rauschen, komplett weglassen“ |
| `hit_zoom`, `hit_deep` | großes Wort / Name rastet ein (sparsam) · `hit_whoosh` ⛔ (Rauschen) |
| `thud_blow`, `thud_wood` | jemand fällt hin, landet, etwas wird abgestellt, Laterne fällt |
| `coins_clink`, `money_bag` | Geld verdienen, kaufen |
| `boom_drum`, `boom_intro` | letzter Schnitt / Ende |
| `camera_shutter` | kommt automatisch auf den Blitz |
- Sounds selbst suchen ist ausdrücklich erlaubt (Deglau): passt nichts aus dem Ordner, auf Mixkit (`mixkit.co/free-sound-effects/<begriff>/`) suchen, zuschneiden, in `_meta.json` eintragen.
- Feedback Video 1: Steam-Achievement bei „größeren Lkw“ war unnötig → Steam-Sounds nur, wenn wirklich „Steam“ gesagt wird.
- Feedback Video 1 (v3): Rauschen/Whooshes komplett weglassen.

### Steam-Logo (Deglau)
- Wenn „Steam“ gesagt wird: `steam_sound` **+ drehendes Steam-Logo** (`assets/steam_logo.png`) – sehr kurz (~0,6 s), dreht sich einmal schnell und bremst ab, ein-/ausblenden.
- Im Schnittplan: `"icons": [{"img": "assets/steam_logo.png", "t": [start, ende], "size": 260, "y": 690, "spin": 1.0}]` – Start ca. 0,05 s vor dem Steam-Sound. Große Wörter vorher enden lassen, damit nichts überlappt.

### Weniger ist mehr (Feedback Video 1, v6)
- Deglau: „Sehr viele Soundeffekte sind unnötig und passen nicht rein.“
- **Nur noch SFX auf klar sichtbare Aktionen** (jemand fällt/landet, etwas wird geworfen, Klick wenn im Menü gewechselt wird, Kauf erscheint, große Wörter, Steam).
- Nicht mehr: Plop auf bloß genannte Wörter (Sofa/Kühlschrank/Klavier), Schrei, Münzen, Boom am Ende, Geräusche auf Dinge, die man nicht klar sieht.
- Richtwert: ca. 10–12 SFX pro 40-s-Video.

### ⭐ So machen wir es ab jetzt (Deglau, nach Video 1) – hat Vorrang vor allen SFX-Regeln oben
- **Musik, Intro (Hintergrundmusik → Tension → Kamera-Auslöser + Blitz → Main Beat) bleiben immer.**
- **Standard-SFX nur noch:**
  - „Steam“ gesagt → `steam_sound` + drehendes Steam-Logo
  - Wechsel/Auswahl in einem Menü, das man im Bild sieht (z. B. Lkw-Shop) → `mouse_click` genau auf jeden Wechsel
- **Alles andere nur, wenn Deglau es ausdrücklich sagt** („bei Sekunde X Sound Y rein“). Nicht selbst zusätzlich einbauen.
