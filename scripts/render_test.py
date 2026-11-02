import json, subprocess, os
from PIL import Image, ImageDraw, ImageFont
S="/tmp/claude-0/-home-user/9a03f581-ea83-5a1f-b271-e1fdeefd0144/scratchpad"; A=S+"/assets"; B=S+"/build"
SRC="/root/.claude/uploads/9a03f581-ea83-5a1f-b271-e1fdeefd0144/c07e4eee-Download_10.mp4"
FLASH=4.72; VOICE=0.0; END=15.0; TS=FLASH-2.0  # TS = Start Spannung

# --- Titel-Box (weiß, abgerundet, 2 Zeilen + Emojis) ---
def title_png(lines, emojis, path):
    f=ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",40)
    ef=ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",109)
    ems=[]
    for e in emojis:
        im=Image.new("RGBA",(140,140)); ImageDraw.Draw(im).text((0,0),e,font=ef,embedded_color=True)
        ems.append(im.crop(im.getbbox()).resize((36,36),Image.LANCZOS))
    ws=[f.getlength(l) for l in lines]; ws[-1]+=len(ems)*40
    W=int(max(ws))+36; H=len(lines)*48+20
    im=Image.new("RGBA",(W,H)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,W-1,H-1),radius=10,fill="white")
    for i,l in enumerate(lines):
        x=(W-ws[i])/2; d.text((x,10+i*48),l,font=f,fill="black")
    x=int((W-ws[-1])/2+f.getlength(lines[-1]))+4
    for e in ems: im.alpha_composite(e,(x,10+(len(lines)-1)*48+6)); x+=40
    im.save(path)
title_png(["Als Schiri das ganze","Match kontrollieren"],["🎮","🔥"],B+"/title.png")

# --- Wörter (Korrekturen der Spracherkennung) ---
words=json.load(open(S+"/words.json"))
fix={"Schiedsie.":"Schiri","Auf":"Ob","Messe":"Messi"}
out=[]
i=0
while i<len(words):
    s,e,w=words[i]
    if w=="d" and i+1<len(words) and words[i+1][2]=="'Or": w="D'OR"; e=words[i+1][1]; i+=1
    w=fix.get(w,w).strip(".,!?").upper()
    out.append((s,e,w)); i+=1
caps=[]
for k,(s,e,w) in enumerate(out):
    nxt=out[k+1][0] if k+1<len(out) else e+0.3
    p=f"{B}/words/{k}.txt"; open(p,"w").write(w)
    caps.append(f"drawtext=fontfile={A}/caption.ttf:textfile={p}:fontsize=84:fontcolor=white:borderw=7:bordercolor=black:"
                f"x=(w-text_w)/2:y=h*0.57:enable='between(t,{VOICE+s:.2f},{VOICE+min(nxt,e+0.4):.2f})'")

zoom=f"(1+if(lt(t,{FLASH}),0.02*t+if(gt(t,{TS}),0.07*(t-{TS})*(t-{TS}),0),0.12*exp(-(t-{FLASH})*6)))"
shake=f"if(between(t,{TS},{FLASH}),9*(t-{TS})*sin(t*70),0)"
v=(f"[0:v]trim=40.5:{40.5+END},setpts=PTS-STARTPTS,delogo=x=246:y=70:w=100:h=84,scale=1080:1920,setsar=1,"
   f"scale=w='trunc(1080*{zoom}/2)*2':h=-2:eval=frame,"
   f"crop=1080:1920:x='(iw-1080)/2+{shake}':y='(ih-1920)/2+{shake.replace('sin(t*70)','cos(t*53)')}',"
   f"eq=brightness='if(between(t,{TS},{FLASH}),-0.15*(t-{TS})/2,0)':eval=frame[g];"
   f"color=white:s=1080x1920:d=0.5,format=rgba,fade=out:st=0.05:d=0.45:alpha=1,setpts=PTS+{FLASH}/TB[fl];"
   f"[g][fl]overlay=eof_action=pass[g2];"
   f"[1:v]scale=175:-1[lg];[g2][lg]overlay=x=(W-w)/2+8:y=128[g3];"
   f"[2:v]format=rgba[tt];[g3][tt]overlay=x=(W-w)/2:y=292:enable='lt(t,{FLASH})',"+",".join(caps)+"[vout]")
fd=int(FLASH*1000)
a=(f"[3:a]atrim=0:{FLASH},volume=-2.5dB,afade=out:st={TS+0.3}:d={FLASH-TS-0.3}[bgm];"
   f"[4:a]atrim=start=11.77:end={11.77+END},asetpts=PTS-STARTPTS,adelay={int(TS*1000)}|{int(TS*1000)},afade=in:st={TS}:d=1.4,"
   f"volume=-13dB,afade=out:st={END-1.2}:d=1.2[beat];"
   f"anoisesrc=d=2:c=pink:a=0.25,highpass=f=2000,afade=in:d=2:curve=exp,adelay={int(TS*1000)}|{int(TS*1000)},aformat=channel_layouts=stereo[rise];"
   f"aevalsrc='0.9*(random(0)*2-1)*(exp(-t*45)+0.7*exp(-max(t-0.07,0)*60)*gte(t,0.07))':d=0.3:s=44100,highpass=f=800,adelay={fd}|{fd},aformat=channel_layouts=stereo[shut];"
   f"[5:a]volume=1.7,aformat=channel_layouts=stereo,adelay={int(VOICE*1000)+1}|{int(VOICE*1000)+1}[vo];"
   f"[bgm][beat][rise][shut][vo]amix=inputs=5:normalize=0,alimiter=limit=0.95[aout]")
open(B+"/graph.txt","w").write(v+";"+a)
cmd=["ffmpeg","-v","error","-y","-i",SRC,"-i",A+"/logo.png","-loop","1","-i",B+"/title.png","-i",A+"/bgm.wav","-i",A+"/beat.wav","-i",S+"/voice_test.wav",
     "-filter_complex_script",B+"/graph.txt","-map","[vout]","-map","[aout]","-t",str(END),"-r","30",
     "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","/home/user/deglau_test_2.mp4"]
subprocess.run(cmd,check=True); print("ok")
