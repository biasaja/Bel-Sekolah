from responsive_voice import ResponsiveVoice
from responsive_voice.voices import IndonesianFemale
engine = ResponsiveVoice()
#indo = IndonesianMale()
indo = IndonesianFemale()
indo.say("Assalamu'alaikum, Selamat Pagi. Pelajaran jam pertama, dimulai. awali dengan, basmallah",blocking=True)
#indo.say("walhamdulillah, program udah bisa berjalan dengan baik",blocking=True)
