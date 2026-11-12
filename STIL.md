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
- Auf Deglaus Ansage (Video 1): **Geld abgezogen → `money_lose`**, **jemand wird getroffen → `scream_kurz` (leise, -4 dB)**, **jemand fällt hin → `bone_crack`** – jeweils genau auf den sichtbaren Moment.
  Diese drei darf ich künftig bei genau solchen Momenten auch von mir aus vorschlagen.
  - Feinschliff (Deglau): Schrei erst **beginnen** lassen, wenn die Figur am Boden liegt (Startzeit, nicht Peak, auf den Moment). Bone Crack ruhig lauter (ca. +4 dB über dem Standard).

## ⭐⭐ AUFGABENTEILUNG (Deglau, final nach Video 1) – gilt vor allem anderen
**Claude macht immer:**
1. **Script schreiben** (Stil siehe oben, Features nur aus dem Trailer).
2. **Video schneiden** auf Deglaus Aufnahme: Szenen passend zum Gesagten, nur Gameplay, Zoom-Stufe 1.5, Logo, Titel-Box, Wort-für-Wort-Untertitel, große Wörter.
3. **Intro immer:** Hintergrundmusik → Tension → Kamera-Auslöser + Blitz → Main Beat (Lautstärken: −2,5 / −13 / −3 dB).
4. **Steam immer:** sobald „Steam“ gesagt wird → `steam_sound` + drehendes Steam-Logo.
5. **Übergänge** (Blitz/Zoom-Punch wie im Intro) darf Claude auch mitten im Video einsetzen, wenn es an einer Stelle gut passt (z. B. Wechsel zu einem Highlight) – sparsam.

**Deglau macht selbst (in CapCut, nachträglich):** alle anderen **Soundeffekte**.
→ Claude baut **keine weiteren SFX** ein (auch keine Klicks, Bone Crack, Schreie usw.), außer Deglau sagt es ausdrücklich für ein bestimmtes Video.

## Referenzvideos 2 (Download_13–17, Mythix / Midsoss) – Stil-Erweiterungen
### Format „Gratis-Spiel vorne + Hauptspiel hinten“ (Deglaus Idee)
- Erst 1–2 **gratis** Spiele (kurz, je ~10–15 s), danach das eigentliche Spiel (länger). Das Gratis-Spiel zieht rein, das Hauptspiel ist der Payoff.
- Hook teasert alles: z. B. „Doppelter **Gratis-Game-Alarm**! Hier sind 3 Spiele, die selbst dein **arbeitsloser Kollege** mit dir zocken kann, weil zwei davon komplett kostenlos sind. Und am Ende …“ (Teaser auf das Hauptspiel).
- Übergänge zwischen Spielen: „Im ersten komplett kostenlosen Spiel …“ / „Im zweiten kostenlosen Spiel …“ / dann das Hauptspiel.
- Einzelnes Gratis-Spiel: „Gratis-Game-Alarm! Dieses neue Spiel kann selbst dein arbeitsloser Kollege mit dir zocken, weil es komplett kostenlos ist – und verdammt gut aussieht.“
- Der Spruch **„perfekt für deine arbeitslosen Freunde / dein arbeitsloser Kollege“** passt immer, wenn ein Spiel gratis ist.
- Gratis-Spiele finden: Steam-Suche `maxprice=free` (+ `specials=1` für zeitweise -100 %), nach Bewertung (≥75 %, genug Reviews) und Release (neu) filtern, lieber Koop/lustig statt der bekannten Riesen (CS2, Apex …).

### Reihen-Animation am Anfang (Titel baut sich auf)
- Große Wörter erscheinen **nacheinander**, jedes kommt anders rein und bleibt stehen, bis der Block komplett ist:
  „2x“ wächst auf (Scale-Pop) → **Steam-Icon mit grünen „-100 %“-Schildern** fliegt von unten rein → „GRATIS“ (gelb/grün) schießt von links rein → „GAME“ fällt von oben → „ALARM“ ploppt von unten. Ganzer Block in ~1,5 s.
- Bei 2 Gratis-Spielen: Bild am Anfang **geteilt (oben Spiel 1, unten Spiel 2)**, Titel-Block in der Mitte.
- Derselbe Effekt mitten im Video für Highlight-Sätze: „SIEHT – VERDAMMT (rot) – GUT AUS“ Wort für Wort, jedes aus einer anderen Richtung.
- Danach ein **Übergang** zum nächsten Abschnitt (heller Lichtblitz / Licht-Leak, Wisch-Unschärfe).

### Fotos / Bilder einblenden
- ✅ **Erlaubt (Deglau):** kleine **Kachel/Kästchen vom Spiel selbst** (Steam-Kapselbild/Header des Spiels), oben als Bild-im-Bild, z. B. wenn der Spielname fällt oder ein Spiel angekündigt wird. Quelle: Steam-API `header_image` / `capsule_image` des Spiels.
- ⛔ **Nicht erlaubt:** Logos von anderen Firmen/Personen (Python-Logo, App-Store-Kachel usw.) und **Meme-/Personenfotos** (z. B. der Mann im Anzug/Kapuze aus dem Mythix-Video).
- Ausnahme, von Deglau ausdrücklich gewollt: das **drehende Steam-Logo** bei „Steam“ (und das Steam-Icon mit „-100 %“ in der Gratis-Animation).
- Weiterhin: keine Vollbild-Titelkarten/Endbilder aus dem Trailer – die Spiel-Kachel ist immer klein über dem Gameplay.

### Weitere Sätze/CTAs aus den Refs
- „Speichert euch das Video, schickt es euren Freunden und lasst schon mal ein Follow da.“
- „Schickt das Video einem Freund, der …“ (passend zum Spiel)
- Frage für Kommentare: „Würdet ihr lieber als X oder als Y spielen? Schreibt's mir in die Kommentare.“
- „Den Playtest könnt ihr auf Steam zocken“ / „… und ist komplett kostenlos.“

### Vergleiche & Streamer (Deglau, ab Video 3)
- Wenn es passt (nicht Pflicht): das Spiel mit **großen, bekannten Spielen oder Shows** vergleichen – „quasi Satisfactory, nur mit …“, „wie Goldrausch in Alaska, nur dass du der Boss bist“, „Low-Budget-Elden-Ring“.
- Sätze wie „man kann ganze Sachen automatisieren“ nur, wenn der Trailer das auch zeigt (sonst stimmt Bild ≠ Text).
- **Streamer-Zeile** („das perfekte Spiel für ___“), wenn ein Streamer gut passt. Claude macht einen Vorschlag, aber keine erfundenen Aussagen über echte Personen (nicht „X spielt das schon“) – im Zweifel Deglau den Namen wählen lassen.

### Videolänge: immer 1 Minute (Deglau, ab Video S.O.N.A.R.)
- Video **immer bis 60 s** laufen lassen, auch wenn Deglau vorher fertig gesprochen hat (TikTok-1-Minuten-Grenze).
- Nach dem letzten Wort: weiter Gameplay-Montage (Schnitte alle ~1,5–2 s, möglichst noch unbenutzte Szenen) mit dem Main Beat, ohne Untertitel; letzter Schnitt ein schönes Bild, Beat blendet zum Schluss aus.
- Im Schnittplan: `"end": 60.0`.
