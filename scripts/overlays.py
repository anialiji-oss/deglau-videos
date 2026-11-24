#!/usr/bin/env python3
"""Einblendungs-Baukasten (Stil wie Guide-TikToks, Deglau 24.11.2026). Erzeugt .mov mit Alpha für "icons" in edit.json.

python3 scripts/overlays.py stamp   "GONE FOREVER" "#FF3B6B" 1.6 out.mov        # schräger Neon-Stempel, knallt rein
python3 scripts/overlays.py counter "+$" 0 3800 2.5 out.mov                    # Geld-Box zählt hoch
python3 scripts/overlays.py things  "MAGAZINE" 0 2 2.0 out.mov                 # Zähler 0 -> 2 "MAGAZINE"
python3 scripts/overlays.py step    3 "RACE GEGEN YAGO" 3.0 out.mov            # Nummer-Kreis + Label-Schild oben links
python3 scripts/overlays.py cta     4.0 out.mov                                # "FOLGEN" + "VIDEO SPEICHERN" mit Hand
python3 scripts/overlays.py place   "EVELYN ANDREWS ANTIQUES" 2.5 out.mov       # gelbes Ortsschild (über Karte legen)
"""
import math, os, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(REPO, "assets", "caption.ttf")
PINK, YEL, GRN, BLK, WHT = (255, 59, 140, 255), (255, 208, 0, 255), (57, 255, 20, 255), (12, 12, 12, 255), (255, 255, 255, 255)
F = lambda s: ImageFont.truetype(FONT, s)


def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3


def hexcol(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def render(fn, dur, size, out, fps=30):
    tmp = tempfile.mkdtemp()
    for f in range(int(round(dur * fps))):
        im = Image.new("RGBA", size, (0, 0, 0, 0)); fn(im, f / fps, dur)
        im.save(os.path.join(tmp, f"{f:04d}.png"))
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(fps), "-i", os.path.join(tmp, "%04d.png"),
                    "-c:v", "qtrle", "-pix_fmt", "argb", out], check=True)
    shutil.rmtree(tmp)


def paste_scaled(dst, src, s, cx, cy, rot=0):
    if rot: src = src.rotate(rot, resample=Image.BICUBIC, expand=True)
    sm = src.resize((max(1, int(src.width * s)), max(1, int(src.height * s))), Image.LANCZOS)
    dst.alpha_composite(sm, (int(cx - sm.width / 2), int(cy - sm.height / 2)))


def fade_out(im, t, dur, d=0.15):
    if t > dur - d:
        a = max(0.0, (dur - t) / d); im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))


def stamp(text, color, dur, out):
    col = hexcol(color); W, H = 1000, 260
    base = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(base)
    s = 96
    while F(s).getlength(text) > W - 120: s -= 4
    tw = F(s).getlength(text); x0 = (W - tw) / 2 - 30
    d.rounded_rectangle([x0, 60, x0 + tw + 60, 200], 22, outline=col, width=9)
    d.text((W / 2, 130), text, font=F(s), fill=col, anchor="mm")
    glow = base.filter(ImageFilter.GaussianBlur(10))
    card = Image.new("RGBA", (W, H), (0, 0, 0, 0)); card.alpha_composite(glow); card.alpha_composite(glow); card.alpha_composite(base)

    def fn(im, t, dur):
        s_ = 1.0 if t > 0.18 else 2.2 - 1.2 * ease(t / 0.18)
        paste_scaled(im, card, s_, W / 2, H / 2 + 60, rot=-6)
        fade_out(im, t, dur)
    render(fn, dur, (W, H + 120), out)


def counter(prefix, a, b, dur, out):
    W, H = 760, 220

    def fn(im, t, dur):
        v = a + (b - a) * ease((t - 0.2) / max(0.4, dur * 0.55))
        txt = f"{prefix}{int(round(v)):,}".replace(",", ".")
        card = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
        d.rounded_rectangle([10, 30, W - 10, H - 30], 30, fill=(10, 40, 18, 235), outline=GRN, width=7)
        d.ellipse([40, 62, 136, 158], fill=GRN); d.text((88, 110), "$", font=F(70), fill=BLK, anchor="mm")
        s = 104
        while F(s).getlength(txt) > W - 200: s -= 4
        d.text((160, 110), txt, font=F(s), fill=GRN, anchor="lm")
        s_ = 1.0 if t > 0.2 else 0.5 + 0.5 * ease(t / 0.2) + 0.06 * math.sin(math.pi * t / 0.2)
        paste_scaled(im, card, s_, W / 2, H / 2)
        fade_out(im, t, dur)
    render(fn, dur, (W, H), out)


def things(label, a, b, dur, out):
    W, H = 520, 300

    def fn(im, t, dur):
        n = a + int((b - a) * min(1.0, max(0.0, (t - 0.25) / max(0.3, dur * 0.5))) + 0.0001)
        card = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
        d.rounded_rectangle([10, 10, W - 10, H - 10], 26, fill=(30, 12, 40, 235), outline=YEL, width=6)
        d.text((W / 2, 128), str(n), font=F(150), fill=YEL, anchor="mm")
        s = 44
        while F(s).getlength(label) > W - 60: s -= 2
        d.text((W / 2, 248), label, font=F(s), fill=WHT, anchor="mm")
        paste_scaled(im, card, 1.0 if t > 0.2 else 0.5 + 0.5 * ease(t / 0.2), W / 2, H / 2)
        fade_out(im, t, dur)
    render(fn, dur, (W, H), out)


def step(num, label, dur, out):
    W, H = 900, 130

    def fn(im, t, dur):
        d = ImageDraw.Draw(im)
        p = ease(t / 0.25)
        r = 46 * (0.6 + 0.4 * p)
        d.ellipse([60 - r, 65 - r, 60 + r, 65 + r], fill=(40, 14, 50, 240), outline=PINK, width=6)
        d.text((60, 65), str(num), font=F(56), fill=WHT, anchor="mm")
        q = ease((t - 0.12) / 0.3)
        if q > 0:
            s = 40
            while F(s).getlength(label) > W - 220: s -= 2
            tw = F(s).getlength(label) + 50
            x = 125 - (1 - q) * 60
            pill = Image.new("RGBA", (int(tw) + 10, 90), (0, 0, 0, 0)); pd = ImageDraw.Draw(pill)
            pd.rounded_rectangle([0, 10, tw, 80], 18, fill=(40, 14, 50, 235), outline=PINK, width=4)
            pd.text((25, 45), label, font=F(s), fill=WHT, anchor="lm")
            pill.putalpha(pill.getchannel("A").point(lambda v: int(v * q)))
            im.alpha_composite(pill, (int(x), 20))
        fade_out(im, t, dur)
    render(fn, dur, (W, H), out)


def cta(dur, out):
    W, H = 900, 300

    def fn(im, t, dur):
        for i, (txt, col, y) in enumerate([("FOLG MIR FÜR MEHR GTA 6", PINK, 70), ("VIDEO SPEICHERN", YEL, 200)]):
            p = ease((t - i * 0.5) / 0.3)
            if p <= 0: continue
            card = Image.new("RGBA", (760, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
            d.rounded_rectangle([5, 5, 755, 105], 50, fill=(20, 14, 30, 235), outline=col, width=6)
            d.text((380, 55), txt, font=F(48), fill=WHT, anchor="mm")
            paste_scaled(im, card, 0.6 + 0.4 * p, W / 2, y)
            # „Hand“: tippender Punkt
            k = (t - i * 0.5 - 0.4)
            if 0 < k < 0.6:
                rr = 18 + 22 * k
                ImageDraw.Draw(im).ellipse([W / 2 + 300 - rr, y + 20 - rr, W / 2 + 300 + rr, y + 20 + rr], outline=WHT, width=5)
        fade_out(im, t, dur)
    render(fn, dur, (W, H), out)


def place(text, dur, out):
    W, H = 900, 150

    def fn(im, t, dur):
        s = 52
        while F(s).getlength(text) > W - 120: s -= 2
        tw = F(s).getlength(text) + 60
        card = Image.new("RGBA", (int(tw) + 10, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
        d.rounded_rectangle([5, 5, tw, 100], 16, fill=YEL, outline=BLK, width=6)
        d.text((tw / 2 + 2, 53), text, font=F(s), fill=BLK, anchor="mm")
        paste_scaled(im, card, 1.0 if t > 0.2 else 0.4 + 0.6 * ease(t / 0.2), W / 2, H / 2, rot=-3)
        fade_out(im, t, dur)
    render(fn, dur, (W, H), out)


if __name__ == "__main__":
    a = sys.argv; k = a[1]
    if k == "stamp": stamp(a[2], a[3], float(a[4]), a[5])
    elif k == "counter": counter(a[2], float(a[3]), float(a[4]), float(a[5]), a[6])
    elif k == "things": things(a[2], int(a[3]), int(a[4]), float(a[5]), a[6])
    elif k == "step": step(a[2], a[3], float(a[4]), a[5])
    elif k == "cta": cta(float(a[2]), a[3])
    elif k == "place": place(a[2], float(a[3]), a[4])
    print("ok", a[-1])
