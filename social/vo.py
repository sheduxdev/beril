import json, base64, urllib.request, sys
K=open(sys.argv[1]).read().strip()
S={
"tr":("5RqXmIU9ikjifeWoXHMG",[
"Gece üç. Biri sitenin kapılarını yokluyor!",
"Peki ya kapıları ilk sen yoklasan?",
"Bu Beril. Bilgisayarında çalışan, açık kaynak bir güvenlik bekçisi. Hiçbir şey dışarı çıkmaz.",
"Önce etrafa bakar: güvenlik başlıkları, çerezler, sertifika, açık yollar ve portlar. Açık kalan kapıları işaretler.",
"Sonra senin izninle gerçekten dener. Kapıyı açabiliyor mu? Açabilirse kanıtını gösterir ve nasıl kapatacağını söyler.",
"Sadece siteler değil. Telefon uygulamaları, programlar, kodda unutulmuş şifreler, güvensiz paketler, yapay zekâyla yazılmış uygulamalar. Hepsini çalıştırmadan inceler.",
"Ve sadece senin evet dediğin yere dokunur. İzin kaydın yoksa deneme yapmaz. Verilerin dışarı çıkmaz, zararlı exploit de üretmez.",
"Sabah yedide raporun hazır: ne buldu, ne kadar emin, nasıl düzeltirsin. Sen de rahat uyursun.",
"Üstelik öğretir de: on pratik lab, yirmi beş haftalık bir plan ve yüz doksan bir yöntem notu.",
"Güçlü olan sensin, Beril sadece yanında. GitHub'da sheduxdev, beril. Hemen dene!"]),
"en":("cgSgspJ2msm6clMCkdW9",[
"It is three in the morning. Someone is trying the doors of your site.",
"What if you tried them first?",
"Meet Beril. An open source security guard that lives on your own machine. Nothing leaves it.",
"First it looks around: security headers, cookies, certificates, exposed paths and ports. It marks every door left open.",
"Then, with your permission, it really tries. Can it open the door? If it can, it shows the proof and tells you how to lock it.",
"Not just websites. Phone apps, programs, passwords forgotten in code, risky packages, AI-written apps. It inspects them all without running them.",
"And it only touches what you said yes to. No permission record, no attempt. Your data never leaves, and it builds no weaponized exploits.",
"By seven in the morning your report is ready: what it found, how sure it is, how to fix it. And you sleep well.",
"It also teaches: ten practice labs, a twenty five week plan and a hundred ninety one method notes.",
"You are the powerful one. Beril is just beside you. GitHub, sheduxdev, beril. Try it now!"])}
VS={"tr":{"stability":.45,"similarity_boost":.8,"style":.35,"use_speaker_boost":True,"speed":1.05},"en":{"stability":.5,"similarity_boost":.8}}
MODEL={"tr":"eleven_multilingual_v2","en":"eleven_multilingual_v2"}
ONLY=sys.argv[2:] or list(S)
for l,(vid,segs) in S.items():
    if l not in ONLY: continue
    text=" ".join(segs); starts=[]; p=0
    for s in segs: starts.append(text.index(s,p)); p=starts[-1]+len(s)
    body=json.dumps({"text":text,"model_id":MODEL[l],"voice_settings":VS[l]}).encode()
    r=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128",body,{"xi-api-key":K,"Content-Type":"application/json"})
    d=json.load(urllib.request.urlopen(r))
    open(f"vo/{l}.mp3","wb").write(base64.b64decode(d["audio_base64"]))
    al=d["alignment"]; t=al["character_start_times_seconds"]; e=al["character_end_times_seconds"]
    json.dump({"starts":[t[i] for i in starts],"end":e[-1],"chars":len(text)},open(f"vo/{l}.json","w"))
    print(l,len(text),[round(t[i],2) for i in starts],round(e[-1],2))
