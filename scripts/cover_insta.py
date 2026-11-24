#!/usr/bin/env python3
"""Instagram-Version vom Titelbild (Deglau 24.11.2026): Instagram schneidet im Profil-Raster auf 3:4 (Mitte) zu,
dadurch ist das normale Titelbild „voll rangezoomt“. Hier wird das ganze Titelbild verkleinert in die 3:4-Mitte gesetzt,
außen herum derselbe Hintergrund unscharf. Ausgabe weiter 1080x1920 (zum Hochladen), wichtig ist nur die Mitte.

Aufruf: python3 scripts/cover_insta.py titelbild.jpg titelbild_insta.jpg
"""
import sys
from PIL import Image, ImageFilter, ImageDraw

W, H, GRID_H = 1080, 1920, 1440   # sichtbarer 3:4-Ausschnitt in der Mitte: y 240..1680


def make(src, out):
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS)
    bg = im.filter(ImageFilter.GaussianBlur(30)).point(lambda v: int(v * 0.55))
    h = GRID_H - 40; w = int(h * W / H)
    small = im.resize((w, h), Image.LANCZOS)
    x, y = (W - w) // 2, (H - h) // 2
    sh = Image.new("L", (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle([x - 6, y - 6, x + w + 6, y + h + 6], 30, fill=200)
    bg.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(20)))
    mask = Image.new("L", (w, h), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, w, h], 28, fill=255)
    bg.paste(small, (x, y), mask)
    bg.save(out, quality=92); print("fertig:", out)


if __name__ == "__main__":
    make(sys.argv[1], sys.argv[2])
