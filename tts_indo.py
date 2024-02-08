from gtts import gTTS
import pygame
import io
import sys
import os

def text_to_speech(text):
    try:
        # Buat objek gTTS
        tts = gTTS(text=text, lang='id')  # 'id' adalah kode bahasa untuk Bahasa Indonesia

        # Simpan suara sintesis sebagai objek BytesIO
        bytes_io = io.BytesIO()
        tts.write_to_fp(bytes_io)

        # Pindahkan kursor ke awal objek BytesIO
        bytes_io.seek(0)

        # Inisialisasi Pygame mixer
        pygame.mixer.init()

        # Baca bytes dan putar audio menggunakan pygame.mixer
        pygame.mixer.music.load(bytes_io)
        pygame.mixer.music.play()

        # Tunggu hingga audio selesai diputar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        # Tangkap pengecualian dan tampilkan pesan
        print(f"Error: {e}")
        print("Pastikan Anda terhubung ke internet untuk menggunakan gTTS.")
        sys.exit(1)

# Loop utama
while True:
    teks_input = input("Masukkan teks: ")
    teks_input = teks_input.replace("*", "").replace("...", "")
    
    if teks_input.lower() == 'cls':
        #text_to_speech('dibersihkan')
        os.system('cls')  # Keluar dari loop jika pengguna memasukkan 'exit'
    
    else:
        text_to_speech(teks_input)
