import sys, wave, json, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
w=wave.open(sys.argv[1]); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
segs,_=m.transcribe(a,language="de",word_timestamps=True, initial_prompt="Fußball, Schiri, Messi, Ronaldo, Ballon d'Or, Elfmeter")
out=[]
for s in segs:
    for x in s.words: out.append([round(x.start,2),round(x.end,2),x.word.strip()])
json.dump(out,open(sys.argv[2],"w"),ensure_ascii=False); print(out)
