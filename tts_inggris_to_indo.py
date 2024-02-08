from gtts import gTTS
import pygame
import io
import sys
import os
from googletrans import Translator

def remove_special_chars(input_text):
    # Remove "*", "...", and "-"
    cleaned_text = input_text.replace("*", ",").replace("...", "").replace("-", "")

    return cleaned_text

def merge_double_letters(input_text):
    result = input_text[0]  # Inisialisasi hasil dengan karakter pertama

    for i in range(1, len(input_text)):
        current_char = input_text[i].lower()

        # Periksa apakah karakter saat ini sama dengan karakter sebelumnya
        if current_char == input_text[i-1].lower() and current_char.isalpha():
            # Tambahkan satu huruf dari huruf ganda ke hasil
            result += current_char
        else:
            result += current_char

    return result

def text_to_speech(text, target_language='id'):
    try:
        translator = Translator()

        # Detect the input language
        input_language = translator.detect(text).lang

        # Translate the text to the target language
        translated_text = translator.translate(text, dest=target_language).text

        # Create gTTS object with the translated text
        tts = gTTS(text=translated_text, lang=target_language)

        # Save synthesized voice as BytesIO object
        bytes_io = io.BytesIO()
        tts.write_to_fp(bytes_io)

        # Reset BytesIO cursor to the beginning
        bytes_io.seek(0)

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Load and play audio using pygame.mixer
        pygame.mixer.music.load(bytes_io)
        pygame.mixer.music.play()

        # Wait until the audio finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        # Capture exception and display the message
        print(f"Error: {e}")
        print("Make sure you are connected to the internet to use gTTS and Google Translate.")
        #sys.exit(1)

# Main loop
while True:
    input_text = input("Enter text: ")

    # Remove "*" and "..."
    input_text = remove_special_chars(input_text)

    # Merge double letters
    input_text = merge_double_letters(input_text)
    print(input_text)

    if input_text.lower() == 'cls':
        os.system('cls')
    else:
        text_to_speech(input_text, target_language='id')  # 'id' is the language code for Indonesian
