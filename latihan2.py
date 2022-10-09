from responsive_voice import ResponsiveVoice
from responsive_voice.voices import IndonesianFemale
from responsive_voice.voices import IndonesianMale
from datetime import datetime
engine = ResponsiveVoice()

weekDays = ("Senin","Selasa","Rabu","Kamis","Juma'at","Sabtu","Ahad")
moonthDays = ("","Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember")

now = datetime.now()
tgl = now.day
bulan = now.month
namabulan = moonthDays[bulan]
hari = now.weekday()
namahari = weekDays[hari]
tahun = now.year
jam = now.hour
menit = now.minute

if jam <=10:
    kondisi="pagi"
elif jam <14:
    kondisi = "siang"
elif jam <=17:
    kondisi = "sore"
else:
    kondisi = "malam"

if menit == 0:
    mnt="tepat"
else:
    mnt="lebih"

indo = IndonesianMale()
print("Assalamu'alaikum, selamat %s, sekarang hari, %s, tanggal %d, bulan %s, tahun %d, dan waktu menunjukkan pukul, %s %s %s menit, Waktu indonesia bagian barat. ai o ti, alias iot, Testing voice bot untuk bel sekolah" %(kondisi,namahari,tgl,namabulan,tahun,jam,mnt,menit))
indo.say("Assalamu'alaikum, selamat %s, sekarang hari, %s, tanggal %d, bulan %s, tahun %d, dan waktu menunjukkan pukul, %s %s %s menit, Waktu indonesia bagian barat. ai o ti, alias iot, Testing voice bot untuk bel sekolah" %(kondisi,namahari,tgl,namabulan,tahun,jam,mnt,menit),blocking=True)

