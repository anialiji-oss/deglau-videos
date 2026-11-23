#!/usr/bin/env python3
"""Animierte Code-Karte (gelb/schwarz wie die Cheat-Karten): Ziffern werden nacheinander langsam „eingetippt“.
Aufruf: python3 scripts/code_card.py "TITEL" CODE DAUER ausgabe.mov [unterzeile]
"""
import math, os, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(REPO, "assets", "caption.ttf")
YEL, BLK, GREY = (255, 208, 0, 255), (12, 12, 12, 255), (60, 60, 60, 255)


def frame(title, code, sub, shown, press_t):
    W, H, box, gap = 980, 330 if sub else 280, 118, 14
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, W - 6, H - 6], 36, fill=YEL, outline=BLK, width=10)
    fs = 74
    while ImageFont.truetype(FONT, fs).getlength(title) > W - 80: fs -= 2
    d.text((W / 2, 68), title, font=ImageFont.truetype(FONT, fs), fill=BLK, anchor="mm")
    toks = code.split(" ") if " " in code else list(code)   # Passwort aus Wörtern: "MUFFINS QUEEN 15"
    fd = ImageFont.truetype(FONT, 92 if " " not in code else 64)
    ws = [max(box, int(fd.getlength(t)) + 44) for t in toks]
    x = (W - (sum(ws) + (len(ws) - 1) * gap)) / 2; y0 = 120; xs = []
    for w_ in ws: xs.append(x + w_ / 2); x += w_ + gap
    for i, ch in enumerate(toks):
        cx, cy = xs[i], y0 + box / 2; bw = ws[i] / 2
        k = 1.0
        if i < shown:
            bg, fg = BLK, YEL
            if i == shown - 1 and press_t is not None and press_t < 1:
                k = 1 - 0.18 * math.sin(math.pi * press_t)
                if press_t < 0.5: bg, fg = (255, 255, 255, 255), BLK
        else:
            bg, fg = GREY, None
        h = box * k / 2; hw = bw * k
        d.rounded_rectangle([cx - hw, cy - h, cx + hw, cy + h], 18, fill=bg)
        if fg:
            d.text((cx, cy + 4), ch, font=fd, fill=fg, anchor="mm")
    if sub:
        f2 = 40
        while ImageFont.truetype(FONT, f2).getlength(sub) > W - 90: f2 -= 2
        d.text((W / 2, 290), sub.upper(), font=ImageFont.truetype(FONT, f2), fill=BLK, anchor="mm")
    return im


def make(title, code, dur, out, sub="", start=0.4, step=0.32, fps=30):
    tmp = tempfile.mkdtemp(); n = len(code.split(" ")) if " " in code else len(code); press = 0.16
    if " " in code: step = 0.5
    for f in range(int(round(dur * fps))):
        t = f / fps
        q = (t - start) / step
        if q < 0:
            im = frame(title, code, sub, 0, None)
        else:
            k = min(n, int(q) + 1); pt = (t - start - (k - 1) * step) / press
            im = frame(title, code, sub, k, pt if pt < 1 else None)
        s = 1.0 if t >= 0.25 else 0.5 + 0.5 * (1 - (1 - t / 0.25) ** 3) + 0.08 * math.sin(math.pi * t / 0.25)
        fr = Image.new("RGBA", im.size, (0, 0, 0, 0))
        sc = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)
        fr.alpha_composite(sc, ((im.width - sc.width) // 2, (im.height - sc.height) // 2))
        fr.save(os.path.join(tmp, f"{f:04d}.png"))
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(fps), "-i", os.path.join(tmp, "%04d.png"),
                    "-c:v", "qtrle", "-pix_fmt", "argb", out], check=True)
    shutil.rmtree(tmp)


if __name__ == "__main__":
    a = sys.argv
    make(a[1], a[2], float(a[3]), a[4], a[5] if len(a) > 5 else "")
    print("ok", a[4])
