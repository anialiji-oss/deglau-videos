#!/usr/bin/env python3
"""Titelbild (1080x1920) für TikTok / Reels / Shorts.

Aufruf: python3 scripts/cover.py videos/<spiel>/cover.json
cover.json:
{
  "video": "sonar.mp4",          # fertiges Video (Logo ist schon drin)
  "time": 54.0,                  # Bild ohne Untertitel (z. B. aus der Gameplay-Montage nach der Stimme)
  "lines": [["EURE FREUNDE", "white"], ["ALS U-BOOT", "#39FF14"], ["CREW", "white"]],
  "card": "spiel_kachel.png",    # optional: Spiel-Kachel
  "output": "titelbild.jpg"
}
Text sitzt im mittleren Bereich, damit TikTok/Instagram-Raster (3:4-Ausschnitt) ihn nicht abschneiden.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(REPO, "assets", "caption.ttf")


def main(path):
    base = os.path.dirname(os.path.abspath(path))
    C = json.load(open(path))
    p = lambda f: f if os.path.isabs(f) else os.path.join(base, f)
    tmp = tempfile.mkdtemp()
    frame = os.path.join(tmp, "f.png")
    if C.get("src"):   # Bild direkt aus dem Trailer, gleicher Aufbau wie im Video (Zoom-Stufe, unscharfer Rand, Logo)
        rx, ry, rw, rh = C.get("rect", [0, 0, 1, 1]); wide = C.get("wide", 1.5)
        vf = (f"crop=trunc(iw*{rw}/2)*2:trunc(ih*{rh}/2)*2:iw*{rx}:ih*{ry},split[a][b];"
              f"[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:2,eq=brightness=-0.08[bg];"
              f"[b]crop='min(iw,trunc(ih*9/16*{wide}/2)*2)':ih:(iw-ow)*{C.get('cx', 0.5)}:0,scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(C["src_time"]), "-i", p(C["src"]),
                        "-frames:v", "1", "-vf", vf, frame], check=True)
        im = Image.open(frame).convert("RGBA")
        logo = Image.open(os.path.join(REPO, "assets", "logo.png")).convert("RGBA")
        logo = logo.resize((175, int(logo.height * 175 / logo.width)), Image.LANCZOS)
        im.alpha_composite(logo, ((im.width - 175) // 2 + 8, 128))
    else:              # Bild aus dem fertigen Video (Stelle ohne Untertitel wählen)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(C["time"]), "-i", p(C["video"]),
                        "-frames:v", "1", frame], check=True)
        im = Image.open(frame).convert("RGBA")
    W, H = im.size
    # leichte Abdunklung zur Mitte hin, damit der Text knallt
    shade = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(shade)
    for y in range(H):
        a = int(150 * max(0, 1 - abs(y - H * 0.47) / (H * 0.33)))
        d.line([(0, y), (W, y)], fill=a)
    im.alpha_composite(Image.composite(Image.new("RGBA", (W, H), (0, 0, 0, 255)),
                                       Image.new("RGBA", (W, H), (0, 0, 0, 0)), shade))
    # Text
    lines = C["lines"]
    size = C.get("size", 150)
    fonts = []
    for txt, _ in lines:
        s = size
        while ImageFont.truetype(FONT, s).getlength(txt) > W * 0.92 and s > 60:
            s -= 4
        fonts.append(ImageFont.truetype(FONT, s))
    hs = [f.getbbox(t, stroke_width=12)[3] - f.getbbox(t, stroke_width=12)[1] for (t, _), f in zip(lines, fonts)]
    gap = 18
    y = int(H * 0.47 - (sum(hs) + gap * (len(lines) - 1)) / 2)
    dr = ImageDraw.Draw(im)
    for (txt, col), f, h in zip(lines, fonts, hs):
        b = f.getbbox(txt, stroke_width=12)
        x = (W - (b[2] - b[0])) / 2 - b[0]
        dr.text((x, y - b[1]), txt, font=f, fill=col, stroke_width=12, stroke_fill="black")
        y += h + gap
    # Spiel-Kachel über dem Text
    if C.get("card"):
        card = Image.open(p(C["card"])).convert("RGBA")
        cw = C.get("card_width", 620)
        card = card.resize((cw, int(card.height * cw / card.width)), Image.LANCZOS)
        top = int(H * 0.47 - (sum(hs) + gap * (len(lines) - 1)) / 2) - card.height - 30
        im.alpha_composite(card, ((W - cw) // 2, max(260, top)))
    out = p(C["output"])
    im.convert("RGB").save(out, quality=92)
    print("fertig:", out)


if __name__ == "__main__":
    main(sys.argv[1])
