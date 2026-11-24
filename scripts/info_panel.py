#!/usr/bin/env python3
"""Info-Box wie in Erklär-TikToks: dunkles Panel oben, Überschrift + Punkte, die nacheinander mit grünem Haken
reinfliegen, während das Gameplay dahinter weiterläuft. Ausgabe: .mov mit Alpha (als "icons"-Eintrag in edit.json).

Aufruf: python3 scripts/info_panel.py panel.json ausgabe.mov
panel.json: {"tag": "NUMMER 1", "title": "WAFFENLADEN", "dur": 5.6,
             "items": [["Waffenschrank", 1.6], ["Varianten", 2.5], ["Gravierte Pistole", 4.8]]}
Zeiten der Items relativ zum Start des Panels (Sekunden).
"""
import json, math, os, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(REPO, "assets", "caption.ttf")
W, ROW = 900, 78


def ease(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def frame(P, t):
    items = P["items"]
    H = 120 + ROW * len(items) + 24
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([4, 4, W - 4, H - 4], 30, fill=(18, 18, 24, 225), outline=(255, 208, 0, 255), width=5)
    ft = ImageFont.truetype(FONT, 54)
    if P.get("tag"):
        fg = ImageFont.truetype(FONT, 30); tw = fg.getlength(P["tag"]) + 36
        d.rounded_rectangle([30, 28, 30 + tw, 76], 16, fill=(255, 208, 0, 255))
        d.text((30 + tw / 2, 52), P["tag"], font=fg, fill=(12, 12, 12, 255), anchor="mm")
        x0 = 30 + tw + 22
    else:
        x0 = 30
    s = 54
    while ImageFont.truetype(FONT, s).getlength(P["title"]) > W - x0 - 30: s -= 2
    d.text((x0, 52), P["title"], font=ImageFont.truetype(FONT, s), fill=(255, 255, 255, 255), anchor="lm")
    fi = ImageFont.truetype(FONT, 44)
    for i, (txt, ti) in enumerate(items):
        y = 120 + i * ROW + ROW / 2
        p = ease((t - ti) / 0.25)
        if p <= 0:
            continue
        off = (1 - p) * 120
        a = int(255 * p)
        row = Image.new("RGBA", (W, ROW), (0, 0, 0, 0)); r = ImageDraw.Draw(row)
        r.rounded_rectangle([24, 6, W - 24, ROW - 6], 18, fill=(255, 255, 255, int(28 * p)))
        cx, cy = 70, ROW / 2
        r.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], fill=(57, 255, 20, 255))
        r.line([(cx - 11, cy + 1), (cx - 3, cy + 10), (cx + 13, cy - 9)], fill=(12, 12, 12, 255), width=7)
        s2 = 44
        while ImageFont.truetype(FONT, s2).getlength(txt) > W - 160: s2 -= 2
        r.text((112, cy), txt, font=ImageFont.truetype(FONT, s2), fill=(255, 255, 255, 255), anchor="lm")
        if a < 255:
            alpha = row.getchannel("A").point(lambda v: v * a // 255); row.putalpha(alpha)
        im.alpha_composite(row, (int(off), int(y - ROW / 2)))
    # Panel poppt rein
    sc = 1.0 if t >= 0.22 else 0.6 + 0.4 * ease(t / 0.22) + 0.05 * math.sin(math.pi * t / 0.22)
    fr = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sm = im.resize((max(1, int(W * sc)), max(1, int(H * sc))), Image.LANCZOS)
    fr.alpha_composite(sm, ((W - sm.width) // 2, 0))
    return fr


def make(P, out, fps=30):
    tmp = tempfile.mkdtemp()
    for f in range(int(round(P["dur"] * fps))):
        frame(P, f / fps).save(os.path.join(tmp, f"{f:04d}.png"))
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(fps), "-i", os.path.join(tmp, "%04d.png"),
                    "-c:v", "qtrle", "-pix_fmt", "argb", out], check=True)
    shutil.rmtree(tmp)


if __name__ == "__main__":
    make(json.load(open(sys.argv[1])), sys.argv[2])
    print("ok", sys.argv[2])
