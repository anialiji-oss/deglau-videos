#!/usr/bin/env python3
"""Deglau-Renderer: baut aus einem Schnittplan (edit.json) das fertige TikTok.

Aufruf:  python3 scripts/render.py videos/<spiel>/edit.json
Der Schnittplan enthält: Voiceover, Wort-Zeitstempel, Quellen (Trailer), Segmente,
Untertitel-Korrekturen, große Wort-Effekte, Soundeffekte. Pfade relativ zum Repo
oder absolut. Lautstärken nach Deglaus CapCut-Werten (STIL.md).
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(REPO, "assets")
W, H, FPS = 1080, 1920, 30
VOL = {"bgm": "-2.5dB", "beat": "-13dB", "sfx": -3.0}   # STIL.md
BEAT_DROP = 13.77                                        # Drop im Main Beat
_META = json.load(open(os.path.join(A, "sfx", "_meta.json")))
def PEAK(name):
    """Sekunde, an der der Sound am lautesten ist (assets/sfx/_meta.json)."""
    return _META.get(name, {}).get("peak", 0.0)


def p(path, base):
    return path if os.path.isabs(path) else os.path.join(base, path)


def run(cmd):
    subprocess.run(cmd, check=True)


# ---------- Grafiken ----------
def title_png(lines, emojis, path):
    f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", 40)
    ef = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)
    ems = []
    for e in emojis:
        im = Image.new("RGBA", (140, 140)); ImageDraw.Draw(im).text((0, 0), e, font=ef, embedded_color=True)
        ems.append(im.crop(im.getbbox()).resize((40, 40), Image.LANCZOS))
    ws = [f.getlength(l) for l in lines]; ws[-1] += len(ems) * 44
    Wb = int(max(ws)) + 40; Hb = len(lines) * 48 + 22
    im = Image.new("RGBA", (Wb, Hb)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, Wb - 1, Hb - 1), radius=12, fill="white")
    for i, l in enumerate(lines):
        d.text(((Wb - ws[i]) / 2, 10 + i * 48), l, font=f, fill="black")
    x = int((Wb - ws[-1]) / 2 + f.getlength(lines[-1])) + 4
    for e in ems:
        im.alpha_composite(e, (x, 10 + (len(lines) - 1) * 48 + 6)); x += 44
    im.save(path)


def word_png(text, color, size, path):
    f = ImageFont.truetype(os.path.join(A, "caption.ttf"), size)
    b = f.getbbox(text, stroke_width=10)
    im = Image.new("RGBA", (b[2] - b[0] + 20, b[3] - b[1] + 20))
    ImageDraw.Draw(im).text((10 - b[0], 10 - b[1]), text, font=f, fill=color, stroke_width=10, stroke_fill="black")
    im.save(path)


# ---------- Untertitel ----------
def build_captions(words, fixes, skip_ranges):
    """fixes: Liste [original, ersatz]; der Reihe nach auf das jeweils nächste passende Wort angewendet.
    ersatz mit Leerzeichen -> Wortdauer wird aufgeteilt; ersatz '' -> Wort entfällt."""
    out, fi = [], 0
    for s, e, w in words:
        w0 = w.strip()
        if fi < len(fixes) and w0.strip(".,!?") == fixes[fi][0]:
            rep = fixes[fi][1]; fi += 1
            if rep == "":
                continue
            parts = rep.split(" ")
            d = (e - s) / len(parts)
            for k, part in enumerate(parts):
                out.append([s + k * d, s + (k + 1) * d, part])
            continue
        out.append([s, e, w0.strip(".,!?\"„“")])
    assert fi == len(fixes), f"Untertitel-Korrektur nicht gefunden: {fixes[fi:]}"
    caps = []
    for k, (s, e, w) in enumerate(out):
        if any(a <= s < b for a, b in skip_ranges):
            continue
        nxt = out[k + 1][0] if k + 1 < len(out) else e + 0.4
        caps.append((s, min(nxt, e + 0.4), w.upper()))
    return caps


def main(edit_path):
    base = os.path.dirname(os.path.abspath(edit_path))
    E = json.load(open(edit_path))
    tmp = tempfile.mkdtemp(prefix="deglau_")
    voice = p(E["voice"], base)
    words = json.load(open(p(E["words"], base)))
    FLASH = E["flash"]; END = E["end"]
    src = {k: p(v, base) for k, v in E["sources"].items()}

    # ---- 1) Segmente einzeln rendern (9:16, exakte Länge) ----
    seg_files = []
    segs = E["segments"]
    for i, sg in enumerate(segs):
        t0, t1 = sg["t"]
        if i + 1 < len(segs):
            t1 = segs[i + 1]["t"][0]          # lückenlos
        else:
            t1 = max(t1, END)
        out_d = t1 - t0
        nfr = round(t1 * FPS) - round(t0 * FPS)
        ss, se = sg["src"][1], sg["src"][2]
        speed = (se - ss) / out_d if se else 1.0
        cx = sg.get("cx", 0.5); zoom = sg.get("zoom", 1.0)
        if "fit" in sg:   # ganzes 16:9-Bild zeigen (Logos/Endbild), unscharfer Hintergrund dahinter
            fw = int(W * sg["fit"]) // 2 * 2
            vf = (f"setpts=(PTS-STARTPTS)/{speed:.5f},split[a][b];"
                  f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=25:2,eq=brightness=-0.08[bg];"
                  f"[b]scale={fw}:-2:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,"
                  f"setsar=1,fps={FPS},tpad=stop_mode=clone:stop_duration=2")
        else:
            vf = (f"setpts=(PTS-STARTPTS)/{speed:.5f},"
                  f"crop=trunc(ih*9/16/{zoom}/2)*2:trunc(ih/{zoom}/2)*2:(iw-ow)*{cx}:(ih-oh)*{sg.get('cy', 0.5)},"
                  f"scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS},tpad=stop_mode=clone:stop_duration=2")
        f = os.path.join(tmp, f"seg{i:03d}.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-i", src[sg["src"][0]], "-an", "-vf", vf,
             "-frames:v", str(nfr), "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-pix_fmt", "yuv420p", f])
        seg_files.append(f)
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{f}'\n" for f in seg_files))
    base_v = os.path.join(tmp, "base.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base_v])

    # ---- 2) Grafiken ----
    title = os.path.join(tmp, "title.png")
    title_png(E["title"]["lines"], E["title"].get("emojis", ["🎮", "🔥"]), title)
    big = []
    for j, bw in enumerate(E.get("bigwords", [])):
        f = os.path.join(tmp, f"big{j}.png"); word_png(bw["text"], bw.get("color", "white"), bw.get("size", 150), f)
        big.append((f, bw))
    skip = [tuple(bw["hide_captions"]) for bw in E.get("bigwords", []) if "hide_captions" in bw]
    caps = build_captions(words, E.get("caption_fixes", []), skip)

    # ---- 3) Video-Filter ----
    TS = FLASH - 2.0
    inputs = ["-i", base_v, "-i", os.path.join(A, "logo.png"), "-loop", "1", "-i", title]
    for f, _ in big:
        inputs += ["-loop", "1", "-i", f]
    zoom = f"(1+if(lt(t,{FLASH}),0.02*t+if(gt(t,{TS}),0.07*(t-{TS})*(t-{TS}),0),0.12*exp(-(t-{FLASH})*6)))"
    shake = f"if(between(t,{TS},{FLASH}),9*(t-{TS})*sin(t*70),0)"
    v = (f"[0:v]scale=w='trunc({W}*{zoom}/2)*2':h=-2:eval=frame,"
         f"crop={W}:{H}:x='(iw-{W})/2+{shake}':y='(ih-{H})/2+{shake.replace('sin(t*70)', 'cos(t*53)')}',"
         f"eq=brightness='if(between(t,{TS},{FLASH}),-0.15*(t-{TS})/2,0)':eval=frame[g0];"
         f"color=white:s={W}x{H}:d=0.5,format=rgba,fade=out:st=0.05:d=0.45:alpha=1,setpts=PTS+{FLASH}/TB[fl];"
         f"[g0][fl]overlay=eof_action=pass[g1];"
         f"[1:v]scale=175:-1[lg];[g1][lg]overlay=x=(W-w)/2+8:y=128[g2];"
         f"[2:v]format=rgba[tt];[g2][tt]overlay=x=(W-w)/2:y=292:enable='lt(t,{FLASH})'[g3]")
    last = "g3"
    for j, (f, bw) in enumerate(big):
        t0, t1 = bw["t"]; y0 = bw["y"]; idx = 3 + j
        if bw.get("anim", "drop") == "drop":      # fällt von oben rein und wippt nach
            y = f"{y0}-700*exp(-7*(t-{t0}))*cos(13*(t-{t0}))"; x = "(W-w)/2"
        else:                                      # 'slide': schießt von rechts rein
            y = str(y0); x = f"(W-w)/2+1100*exp(-9*(t-{t0}))*cos(9*(t-{t0}))"
        v += f";[{idx}:v]format=rgba[b{j}];[{last}][b{j}]overlay=x='{x}':y='{y}':enable='between(t,{t0},{t1})'[k{j}]"
        last = f"k{j}"
    cdir = os.path.join(tmp, "w"); os.makedirs(cdir)
    dt = []
    for k, (s, e, w) in enumerate(caps):
        tf = os.path.join(cdir, f"{k}.txt"); open(tf, "w").write(w)
        dt.append(f"drawtext=fontfile={A}/caption.ttf:textfile={tf}:fontsize=84:fontcolor=white:borderw=7:bordercolor=black:"
                  f"x=(w-text_w)/2:y=h*0.57:enable='between(t,{s:.2f},{e:.2f})'")
    v += f";[{last}]" + ",".join(dt) + "[vout]"

    # ---- 4) Audio ----

    ai = ["-i", voice, "-i", os.path.join(A, "musik", "hintergrund_musik.mp3"),
          "-i", os.path.join(A, "musik", "mainbeat.mp3"), "-i", os.path.join(A, "sfx", "tension.mp3")]
    n0 = 3 + len(big)                     # Index der Voice-Eingabe
    ms = lambda t: max(0, int(round(t * 1000)))
    a = (f"[{n0}:a]aformat=sample_rates=48000:channel_layouts=stereo[vo];"
         f"[{n0+1}:a]atrim=0:{FLASH},volume={VOL['bgm']},afade=out:st={FLASH-0.15}:d=0.15,aformat=sample_rates=48000:channel_layouts=stereo[bgm];"
         f"[{n0+2}:a]atrim=start={BEAT_DROP}:end={BEAT_DROP+END-FLASH+0.1},asetpts=PTS-STARTPTS,volume={VOL['beat']},"
         f"afade=out:st={END-FLASH-1.2}:d=1.2,adelay={ms(FLASH)}|{ms(FLASH)},aformat=sample_rates=48000:channel_layouts=stereo[beat];"
         f"[{n0+3}:a]volume={VOL['sfx']}dB,adelay={ms(FLASH-PEAK('tension'))}|{ms(FLASH-PEAK('tension'))},aformat=sample_rates=48000:channel_layouts=stereo[ten]")
    mix = ["vo", "bgm", "beat", "ten"]
    # Kamera-Auslöser auf dem Blitz (Datei aus assets/sfx, Peak auf den Blitz gelegt)
    sfx_list = [["camera_shutter", FLASH]] + E.get("sfx", [])
    sfx_in = []
    for k, (name, t, *extra) in enumerate(sfx_list):
        sfx_in += ["-i", os.path.join(A, "sfx", name + ".mp3")]
        db = VOL["sfx"] + (extra[0] if extra else 0)
        st = t - PEAK(name)                # t = Zeitpunkt, an dem der Sound am lautesten sein soll
        a += f";[{n0+4+k}:a]volume={db}dB,adelay={ms(st)}|{ms(st)},aformat=sample_rates=48000:channel_layouts=stereo[s{k}]"
        mix.append(f"s{k}")
    a += ";" + "".join(f"[{m}]" for m in mix) + f"amix=inputs={len(mix)}:normalize=0:duration=longest,atrim=0:{END},alimiter=limit=0.95[aout]"

    graph = os.path.join(tmp, "graph.txt"); open(graph, "w").write(v + ";" + a)
    out = p(E["output"], base)
    run(["ffmpeg", "-v", "error", "-y", *inputs, *ai, *sfx_in, "-filter_complex_script", graph,
         "-map", "[vout]", "-map", "[aout]", "-t", str(END), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
    print("fertig:", out)


if __name__ == "__main__":
    main(sys.argv[1])
