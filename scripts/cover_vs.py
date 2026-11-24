#!/usr/bin/env python3
"""Titelbild „A vs. B“ (Deglau 24.11.2026): zwei Szenen übereinander, die Autos/Sachen groß im Vordergrund,
oben + unten je ein Titel, in der Mitte ein „VS“-Kreis.

Aufruf: python3 scripts/cover_vs.py cover_vs.json
{
 "top":    {"src": "a.mp4", "time": 2.0, "cx": 0.66, "cy": 0.55, "zoom": 1.0, "label": "FERRARI MIT NITRO", "color": "#FF3B8C"},
 "bottom": {"src": "b.mp4", "time": 5.0, "cx": 0.41, "cy": 0.55, "zoom": 1.0, "label": "BUGATTI", "color": "#3FC5FF"},
 "output": "titelbild.jpg"
}
"rect": [x,y,w,h] optional = Ausschnitt vorab (Menütexte weg). cx/cy = Mitte des Ausschnitts im Originalbild (0–1), zoom > 1 = näher ran.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(REPO, "assets", "caption.ttf")
W, H, HALF = 1080, 1920, 960


def grab(base, P, w, h):
    f = os.path.join(tempfile.mkdtemp(), "f.png")
    src = P["src"] if os.path.isabs(P["src"]) else os.path.join(base, P["src"])
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(P["time"]), "-i", src, "-frames:v", "1", f], check=True)
    im = Image.open(f).convert("RGB")
    if P.get("rect"):  # Ausschnitt vorab (Anteile x,y,w,h), z. B. Menüs/Tab-Leisten wegschneiden
        rx, ry, rw, rh = P["rect"]; W0, H0 = im.size
        im = im.crop((int(rx * W0), int(ry * H0), int((rx + rw) * W0), int((ry + rh) * H0)))
    iw, ih = im.size
    ch = ih / P.get("zoom", 1.0); cw = ch * w / h
    if cw > iw: cw = iw; ch = cw * h / w
    x = min(max(P.get("cx", 0.5) * iw - cw / 2, 0), iw - cw); y = min(max(P.get("cy", 0.5) * ih - ch / 2, 0), ih - ch)
    return im.crop((int(x), int(y), int(x + cw), int(y + ch))).resize((w, h), Image.LANCZOS)


def label(img, text, color, cy):
    d = ImageDraw.Draw(img); s = 140
    while ImageFont.truetype(FONT, s).getlength(text) > W * 0.92: s -= 4
    f = ImageFont.truetype(FONT, s)
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).text((W / 2, cy), text, font=f, fill=color, anchor="mm", stroke_width=18, stroke_fill=color)
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(16)))
    d.text((W / 2, cy), text, font=f, fill="white", anchor="mm", stroke_width=12, stroke_fill="black")
    d.text((W / 2, cy), text, font=f, fill=color, anchor="mm")


def main(path):
    base = os.path.dirname(os.path.abspath(path)); C = json.load(open(path))
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    im.paste(grab(base, C["top"], W, HALF), (0, 0)); im.paste(grab(base, C["bottom"], W, H - HALF), (0, HALF))
    d = ImageDraw.Draw(im)
    d.rectangle([0, HALF - 7, W, HALF + 7], fill=(255, 208, 0, 255))
    # leichte Abdunklung oben/unten, damit die Titel knallen
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    for y in range(0, 520): sd.line([(0, y), (W, y)], fill=(0, 0, 0, int(150 * (1 - y / 520))))
    for y in range(H - 560, H): sd.line([(0, y), (W, y)], fill=(0, 0, 0, int(150 * (y - (H - 560)) / 560)))
    im.alpha_composite(sh)
    label(im, C["top"]["label"], C["top"].get("color", "#FF3B8C"), C.get("top_label_y", 340))
    label(im, C["bottom"]["label"], C["bottom"].get("color", "#3FC5FF"), C.get("bottom_label_y", 1780))
    r = 110
    d.ellipse([W / 2 - r, HALF - r, W / 2 + r, HALF + r], fill=(255, 208, 0, 255), outline=(12, 12, 12, 255), width=10)
    d.text((W / 2, HALF + 4), "VS", font=ImageFont.truetype(FONT, 120), fill=(12, 12, 12, 255), anchor="mm")
    logo = Image.open(os.path.join(REPO, "assets", "logo.png")).convert("RGBA")
    logo = logo.resize((175, int(logo.height * 175 / logo.width)), Image.LANCZOS)
    im.alpha_composite(logo, ((W - 175) // 2 + 8, 110))
    out = C["output"] if os.path.isabs(C["output"]) else os.path.join(base, C["output"])
    im.convert("RGB").save(out, quality=92); print("fertig:", out)


if __name__ == "__main__":
    main(sys.argv[1])
