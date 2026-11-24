#!/usr/bin/env bash
# Kullanım: ./mix-music.sh tr|en /yol/muzik.mp3 [muzik-baslangic-saniyesi]
# Müziği videoya ekler: başta/sonda yumuşak fade, konuşma sırasında kısılır (ducking), -14 LUFS.
set -euo pipefail
L=${1:?tr veya en}; M=${2:?müzik dosyası}; SS=${3:-0}
D="$(cd "$(dirname "$0")" && pwd)/video"
IN="$D/beril-$L-916-nomusic.mp4"; OUT="$D/beril-$L-916.mp4"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
ffmpeg -y -loglevel error -i "$IN" -ss "$SS" -stream_loop -1 -i "$M" -filter_complex \
"[0:a]asplit[vo][sc];[1:a]atrim=0:$DUR,asetpts=PTS-STARTPTS,afade=t=in:d=1.2,afade=t=out:st=$(python3 -c "print(max(0,$DUR-2.5))"):d=2.5,volume=0.5[m];\
[m][sc]sidechaincompress=threshold=0.015:ratio=10:attack=15:release=600[md];\
[vo][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89,loudnorm=I=-14:TP=-1.5[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t "$DUR" -movflags +faststart "$OUT"
echo "tamam: $OUT"
