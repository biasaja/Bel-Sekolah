from responsive_voice import ResponsiveVoice
from responsive_voice.voices import IndonesianMale as cowok
from responsive_voice.voices import IndonesianFemale as cewek
from datetime import datetime
#import gc
import time
import os
import vlc

weekDays = ("Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Minggu")
moonthDays = ("","Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember")

engine = ResponsiveVoice()

now = datetime.now()
tgl = now.day
bulan = now.month
namabulan = moonthDays[bulan]
hari = now.weekday()
namahari = weekDays[hari]
tahun = now.year
jam = now.hour
menit = now.minute

if menit == 0:
    waktu = now.strftime("%H tepat") .lstrip("0").replace(" 0", " ")
else:
    waktu = now.strftime("%H lebih %M menit") .lstrip("0").replace(" 0", " ")


if jam <=10:
    kondisi="Pagi"
elif jam <14:
    kondisi="siang"
elif jam <18:
    kondisi="sore"
else:
    kondisi="malam"

#print("Assalamu'alaikum, selamat %s, sekarang hari, %s, tanggal %d, bulan %s, tahun %d, dan waktu menunjukkan pukul, %s, Waktu indonesia bagian barat. ai o ti, alias iot, Testing voice bot untuk bel sekolah" %(kondisi,namahari,tgl,namabulan,tahun,waktu))

def gender():
    indo = xxx()    
    indo.say("Assalamu'alaikum, selamat %s, sekarang hari, %s, tanggal %d, bulan %s, tahun %d, dan waktu menunjukkan pukul, %s, Waktu indonesia bagian barat. ai o ti, alias iot, Testing voice bot untuk bel sekolah" %(kondisi,namahari,tgl,namabulan,tahun,waktu),blocking=True)


bg = 0
bg = tgl % 2
if bg == 1:
    xxx = cowok
    gender()
else:
    print("genap")
    xxx = cewek
    gender()


if hari == 1:
    media = vlc.MediaPlayer("pancasila.mp3")
    media.play()
    time.sleep(58)
    media.release()
elif hari == 3:
    media = vlc.MediaPlayer("indonesia.mp3")
    media.play()
    time.sleep(130)
    media.release()
else:
    print("other day")
 
    
print("Assalamu'alaikum, selamat", kondisi," sekarang hari", namahari, "tanggal", tgl,
      "bulan", namabulan, "tahun", tahun, "dan waktu menunjukkan pukul", jam,":",menit, "Waktu indonesia bagian barat. ai o ti, alias iot, Testing voice bot untuk bel sekolah")
print("Tanggal : ", tgl)
print("Bulan :", namabulan)
print("tahun :", tahun)
print("jam :", jam)
print("menit :", menit)
print("hari :", namahari)
print("jam :", waktu)

print("Assalamu'alaikum, selamat %s, sekarang hari, %s, tanggal %d, bulan %s, tahun %d, dan waktu menunjukkan pukul, %s, Waktu indonesia bagian barat. ai o ti, alias iot, Testing voice bot untuk bel sekolah" %(kondisi,namahari,tgl,namabulan,tahun,waktu))
