#!/usr/bin/env python3
"""Cheat-Karten (gelb/schwarz, Steuerkreuz-Pfeile) für das GTA-6-Cheats-Video."""
import json, math, os, shutil, subprocess, sys, tempfile
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

def arrow(d, cx, cy, r, direction, col=YEL):
    # Pfeil nach oben, dann drehen
    pts = [(0, -1), (0.75, -0.05), (0.3, -0.05), (0.3, 0.85), (-0.3, 0.85), (-0.3, -0.05), (-0.75, -0.05)]
    rot = {"U": lambda x, y: (x, y), "D": lambda x, y: (-x, -y), "R": lambda x, y: (-y, x), "L": lambda x, y: (y, -x)}[direction]
    d.polygon([(cx + rot(x, y)[0] * r, cy + rot(x, y)[1] * r) for x, y in pts], fill=col)

DIM = (70, 70, 70, 255)

def card(title, unlock, code, pressed=None, press_t=None):
    """pressed: Anzahl schon gedrückter Pfeile (None = alle); press_t: 0..1 Fortschritt des aktuellen Drucks."""
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
    n_on = len(code) if pressed is None else pressed
    for i, c in enumerate(code):
        x = x0 + i * (box + gap); cx, cy = x + box / 2, y0 + box / 2
        if i < n_on:
            k = 1.0; bg, fg = BLK, YEL
            if press_t is not None and i == n_on - 1 and press_t < 1:   # gerade gedrückt: eindrücken + weiß aufleuchten
                k = 1 - 0.18 * math.sin(math.pi * press_t)
                bg, fg = ((255, 255, 255, 255), BLK) if press_t < 0.6 else (BLK, YEL)
        else:
            k = 1.0; bg, fg = (45, 45, 45, 255), (120, 120, 120, 255)
        h = box * k / 2
        d.rounded_rectangle([cx - h, cy - h, cx + h, cy + h], 16, fill=bg)
        arrow(d, cx, cy, box * 0.36 * k, c, fg)
    t2 = "FREISCHALTEN: " + unlock.upper(); fs2 = 40
    while ImageFont.truetype(FONT, fs2).getlength(t2) > W - 90: fs2 -= 2
    d.text((W / 2, 270), t2, font=ImageFont.truetype(FONT, fs2), fill=BLK, anchor="mm")
    return im


def animate(key, dur, fps=30):
    """Karte poppt rein, dann werden die Pfeile nacheinander 'gedrückt'. Ausgabe: karten/<key>.mov (mit Alpha)."""
    title, unlock, code = CARDS[key]
    n = len(code); start = 0.3; step = min(0.2, (dur - 0.9) / n); press = 0.14
    tmp = tempfile.mkdtemp()
    for f in range(int(round(dur * fps))):
        t = f / fps
        q = (t - start) / step
        if q < 0:
            im = card(title, unlock, code, 0)
        else:
            k = min(n, int(q) + 1); pt = (t - start - (k - 1) * step) / press
            im = card(title, unlock, code, k, pt if pt < 1 else None)
        s = 1.0 if t >= 0.25 else 0.5 + 0.5 * (1 - (1 - t / 0.25) ** 3) + 0.08 * math.sin(math.pi * t / 0.25)
        fr = Image.new("RGBA", im.size, (0, 0, 0, 0))
        sc = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)
        fr.alpha_composite(sc, ((im.width - sc.width) // 2, (im.height - sc.height) // 2))
        fr.save(os.path.join(tmp, f"{f:04d}.png"))
    out = os.path.join(HERE, "karten", key + ".mov")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(fps), "-i", os.path.join(tmp, "%04d.png"),
                    "-c:v", "qtrle", "-pix_fmt", "argb", out], check=True)
    shutil.rmtree(tmp)


def hook_panel(keys, dur, fps=30, out_name="hook"):
    """Liste für den Hook: mehrere Cheats untereinander, Codes werden schnell nacheinander 'eingetippt'."""
    W, box, gap, rh = 980, 54, 6, 104
    H = 110 + rh * len(keys) + 20
    rows = [CARDS[k] for k in keys]
    total = sum(len(c) for _, _, c in rows); step = (dur - 0.5) / total; press = 0.09
    fT = ImageFont.truetype(FONT, 64)
    tmp = tempfile.mkdtemp()
    for f in range(int(round(dur * fps))):
        t = f / fps
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle([6, 6, W - 6, H - 6], 34, fill=(10, 10, 10, 225), outline=YEL, width=8)
        d.rounded_rectangle([6, 6, W - 6, 100], 34, fill=YEL)
        d.rectangle([6, 60, W - 6, 100], fill=YEL)
        d.text((W / 2, 55), "GTA 6 CHEATS", font=fT, fill=BLK, anchor="mm")
        done = (t - 0.15) / step if t > 0.15 else -1
        idx = 0
        for r, (title, _, code) in enumerate(rows):
            y = 112 + r * rh; cy = y + rh / 2; title = title.replace("UNENDLICH ", "")
            fs = 40
            while ImageFont.truetype(FONT, fs).getlength(title) > 270: fs -= 2
            d.text((40, cy), title, font=ImageFont.truetype(FONT, fs), fill=(255, 255, 255, 255), anchor="lm")
            n = len(code); x0 = W - 36 - n * box - (n - 1) * gap
            for i, c in enumerate(code):
                cx = x0 + i * (box + gap) + box / 2
                q = done - idx
                if q >= 0:
                    pt = q * step / press
                    k = 1 - 0.2 * math.sin(math.pi * pt) if pt < 1 else 1
                    bg, fg = ((255, 255, 255, 255), BLK) if pt < 0.6 else (YEL, BLK)
                else:
                    k, bg, fg = 1, (50, 50, 50, 255), (130, 130, 130, 255)
                h = box * k / 2
                d.rounded_rectangle([cx - h, cy - h, cx + h, cy + h], 12, fill=bg)
                arrow(d, cx, cy, box * 0.36 * k, c, fg)
                idx += 1
        sc = 1.0 if t >= 0.2 else 0.6 + 0.4 * (1 - (1 - t / 0.2) ** 3)
        fr = Image.new("RGBA", im.size, (0, 0, 0, 0))
        im2 = im.resize((int(W * sc), int(H * sc)), Image.LANCZOS)
        fr.alpha_composite(im2, ((W - im2.width) // 2, (H - im2.height) // 2))
        fr.save(os.path.join(tmp, f"{f:04d}.png"))
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(fps), "-i", os.path.join(tmp, "%04d.png"),
                    "-c:v", "qtrle", "-pix_fmt", "argb", os.path.join(HERE, "karten", out_name + ".mov")], check=True)
    shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "hook":
        hook_panel(["geld", "munition", "weste"], float(sys.argv[2])); print("ok"); sys.exit()
    for key, (title, unlock, code) in CARDS.items():
        card(title, unlock, code).save(os.path.join(HERE, "karten", key + ".png"))
    for key, dur in json.loads(sys.argv[1]).items() if len(sys.argv) > 1 else []:
        animate(key, dur)
    print("ok")
