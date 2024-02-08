import pyttsx3
import os

# Inisialisasi engine TTS
engine = pyttsx3.init()

# Mendapatkan daftar voice yang tersedia
voices = engine.getProperty('voices')

# Memilih suara cewek (index dapat berbeda tergantung pada sistem)
engine.setProperty('voice', voices[2].id)

while 1:
    # Menentukan teks yang akan diucapkan
    text_to_speak = input("Text:")
    if text_to_speak == "cls":
        os.system('cls')
    else:

        # Mengatur kecepatan ucapan (opsional)
        engine.setProperty('rate', 120)

        # Mengatur volume suara (opsional)
        engine.setProperty('volume', 1.0)

        # Memainkan TTS
        engine.say(text_to_speak)

        # Menunggu hingga selesai
        engine.runAndWait()
