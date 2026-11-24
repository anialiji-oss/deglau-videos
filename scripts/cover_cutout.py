#!/usr/bin/env python3
"""Titelbild mit ausgeschnittenen Autos/Sachen + dickem weißen Sticker-Rand (Deglau 24.11.2026).
Beide (oder mehr) Objekte in EINEM Bild, stechen raus. Freistellen mit rembg (pip install "rembg[cpu]").

Aufruf: python3 scripts/cover_cutout.py cover_cutout.json
{
 "background": {"src": "clip.mp4", "time": 3.0, "blur": 14, "dark": 0.45},
 "objects": [
   {"src": "a.mp4", "time": 1.5, "x": 560, "y": 640, "width": 1150, "flip": true, "rot": -4},
   {"src": "b.mp4", "time": 5.0, "x": 520, "y": 1230, "width": 1100, "rot": 3}
 ],
 "texts": [{"text": "FERRARI MIT NITRO", "color": "#FF3B8C", "y": 330}, {"text": "BUGATTI", "color": "#3FC5FF", "y": 1560}],
 "vs": {"x": 540, "y": 960},
 "output": "titelbild.jpg"
}
x/y = Mitte des Objekts im 1080x1920-Bild, width = Breite des Objekts.
"""
import json, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(REPO, "assets", "caption.ttf")
W, H = 1080, 1920


def frame(base, src, t):
    f = os.path.join(tempfile.mkdtemp(), "f.png")
    src = src if os.path.isabs(src) else os.path.join(base, src)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", f], check=True)
    return Image.open(f).convert("RGB")


def cutout(img, session):
    from rembg import remove
    from scipy import ndimage
    a = np.array(remove(img, session=session).getchannel("A"))
    m = a > 140
    lab, n = ndimage.label(m)
    if n > 1:  # nur das größte Stück behalten (Menü-Reste, Boden-Spiegelungen weg)
        sizes = ndimage.sum(m, lab, range(1, n + 1)); m = lab == (1 + int(np.argmax(sizes)))
    m = ndimage.binary_fill_holes(m)
    alpha = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.2))
    out = img.convert("RGBA"); out.putalpha(alpha)
    return out.crop(alpha.getbbox())


def sticker(obj, stroke=16):
    pad = stroke * 3
    big = Image.new("RGBA", (obj.width + 2 * pad, obj.height + 2 * pad), (0, 0, 0, 0)); big.alpha_composite(obj, (pad, pad))
    a = big.getchannel("A").point(lambda v: 255 if v > 100 else 0)
    ring = a.filter(ImageFilter.MaxFilter(2 * stroke + 1)).filter(ImageFilter.GaussianBlur(1.5))
    shadow = ring.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(18))
    out = Image.new("RGBA", big.size, (0, 0, 0, 0))
    sh = Image.new("RGBA", big.size, (0, 0, 0, 255)); sh.putalpha(shadow.point(lambda v: int(v * 0.8)))
    out.alpha_composite(sh, (0, 0))
    wh = Image.new("RGBA", big.size, (255, 255, 255, 255)); wh.putalpha(ring)
    out.alpha_composite(wh); out.alpha_composite(big)
    return out


def label(img, text, color, cy, size=150):
    d = ImageDraw.Draw(img); s = size
    while ImageFont.truetype(FONT, s).getlength(text) > W * 0.92: s -= 4
    f = ImageFont.truetype(FONT, s)
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).text((W / 2, cy), text, font=f, fill=color, anchor="mm", stroke_width=20, stroke_fill=color)
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(18)))
    d.text((W / 2, cy), text, font=f, fill="white", anchor="mm", stroke_width=13, stroke_fill="black")
    d.text((W / 2, cy), text, font=f, fill=color, anchor="mm")


def main(path):
    from rembg import new_session
    base = os.path.dirname(os.path.abspath(path)); C = json.load(open(path))
    B = C["background"]; bg = frame(base, B["src"], B["time"])
    if B.get("rect"):  # Ausschnitt vorab (x,y,w,h Anteile), z. B. Einblendungen unten wegschneiden
        rx, ry, rw, rh = B["rect"]; bg = bg.crop((int(rx * bg.width), int(ry * bg.height), int((rx + rw) * bg.width), int((ry + rh) * bg.height)))
    s = max(W / bg.width, H / bg.height); bg = bg.resize((int(bg.width * s) + 1, int(bg.height * s) + 1), Image.LANCZOS)
    bx = int((bg.width - W) * B.get("cx", 0.5)); bg = bg.crop((bx, 0, bx + W, H)).filter(ImageFilter.GaussianBlur(B.get("blur", 14)))
    im = bg.convert("RGBA")
    # Farbverlauf oben (Farbe Titel 1) -> unten (Farbe Titel 2) + abdunkeln
    tx = C.get("texts", [])
    c1 = tx[0]["color"] if tx else "#FF3B8C"; c2 = tx[-1]["color"] if tx else "#3FC5FF"
    h2rgb = lambda h: tuple(int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    r1, r2 = np.array(h2rgb(c1)), np.array(h2rgb(c2))
    yy = np.linspace(0, 1, H)[:, None, None]
    tint = (r1 * (1 - yy) + r2 * yy) * np.ones((1, W, 1))
    arr = np.array(im.convert("RGB")).astype(float) * (1 - B.get("dark", 0.45))
    arr = arr * 0.75 + tint * 0.25 * (1 - B.get("dark", 0.45) / 2)
    im = Image.fromarray(np.clip(arr, 0, 255).astype("uint8")).convert("RGBA")
    sess = new_session(C.get("model", "isnet-general-use"))
    for O in C["objects"]:
        o = cutout(frame(base, O["src"], O["time"]), sess)
        if O.get("bright"):  # dunkle Szenen aufhellen
            from PIL import ImageEnhance
            a_ = o.getchannel("A"); o = ImageEnhance.Brightness(o.convert("RGB")).enhance(O["bright"]).convert("RGBA"); o.putalpha(a_)
        if O.get("flip"): o = o.transpose(Image.FLIP_LEFT_RIGHT)
        o = o.resize((O["width"], int(o.height * O["width"] / o.width)), Image.LANCZOS)
        st = sticker(o, O.get("stroke", 16))
        if O.get("rot"): st = st.rotate(O["rot"], resample=Image.BICUBIC, expand=True)
        im.alpha_composite(st, (int(O["x"] - st.width / 2), int(O["y"] - st.height / 2)))
    for T in tx: label(im, T["text"], T["color"], T["y"], T.get("size", 150))
    if C.get("vs"):
        d = ImageDraw.Draw(im); x, y, r = C["vs"]["x"], C["vs"]["y"], C["vs"].get("r", 115)
        d.ellipse([x - r - 10, y - r - 10, x + r + 10, y + r + 10], fill=(255, 255, 255, 255))
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 208, 0, 255), outline=(12, 12, 12, 255), width=10)
        d.text((x, y + 4), "VS", font=ImageFont.truetype(FONT, 125), fill=(12, 12, 12, 255), anchor="mm")
    logo = Image.open(os.path.join(REPO, "assets", "logo.png")).convert("RGBA")
    logo = logo.resize((175, int(logo.height * 175 / logo.width)), Image.LANCZOS)
    im.alpha_composite(logo, ((W - 175) // 2 + 8, 100))
    out = C["output"] if os.path.isabs(C["output"]) else os.path.join(base, C["output"])
    im.convert("RGB").save(out, quality=92); print("fertig:", out)


if __name__ == "__main__":
    main(sys.argv[1])
