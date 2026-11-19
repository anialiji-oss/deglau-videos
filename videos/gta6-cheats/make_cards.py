#!/usr/bin/env python3
"""Cheat-Karten (gelb/schwarz, Steuerkreuz-Pfeile) für das GTA-6-Cheats-Video."""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "..", "..", "assets", "caption.ttf")
CARDS = {
    "geld":      ("250.000 $",          "Story durchspielen",        "URDLULDR"),
    "weste":     ("SCHUTZWESTE",        "100 Workouts",              "DULUUUUUDD"),
    "munition":  ("UNENDLICH MUNITION", "25x Silber am Schießstand", "DURDLLUDDD"),
    "nachladen": ("KEIN NACHLADEN",     "25x Gold am Schießstand",   "DURDLLUDDU"),
    "polizei":   ("MEHR POLIZEI",       "25x 3 Sterne abschütteln",  "LDRDUDU"),
}
YEL, BLK = (255, 208, 0, 255), (12, 12, 12, 255)

def arrow(d, cx, cy, r, direction):
    # Pfeil nach oben, dann drehen
    pts = [(0, -1), (0.75, -0.05), (0.3, -0.05), (0.3, 0.85), (-0.3, 0.85), (-0.3, -0.05), (-0.75, -0.05)]
    rot = {"U": lambda x, y: (x, y), "D": lambda x, y: (-x, -y), "R": lambda x, y: (-y, x), "L": lambda x, y: (y, -x)}[direction]
    d.polygon([(cx + rot(x, y)[0] * r, cy + rot(x, y)[1] * r) for x, y in pts], fill=YEL)

for key, (title, unlock, code) in CARDS.items():
    W, box, gap = 980, 84, 8
    H = 330
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, W - 6, H - 6], 36, fill=YEL, outline=BLK, width=10)
    fs = 78
    while ImageFont.truetype(FONT, fs).getlength(title) > W - 80: fs -= 2
    f = ImageFont.truetype(FONT, fs)
    d.text((W / 2, 70), title, font=f, fill=BLK, anchor="mm")
    n = len(code); tw = n * box + (n - 1) * gap; x0 = (W - tw) / 2; y0 = 128
    for i, c in enumerate(code):
        x = x0 + i * (box + gap)
        d.rounded_rectangle([x, y0, x + box, y0 + box], 16, fill=BLK)
        arrow(d, x + box / 2, y0 + box / 2, box * 0.36, c)
    t2 = "FREISCHALTEN: " + unlock.upper(); fs2 = 40
    while ImageFont.truetype(FONT, fs2).getlength(t2) > W - 90: fs2 -= 2
    d.text((W / 2, 270), t2, font=ImageFont.truetype(FONT, fs2), fill=BLK, anchor="mm")
    im.save(os.path.join(HERE, "karten", key + ".png"))
print("ok")
