from gtts import gTTS
import os

def generate_voiceover(script):
    tts = gTTS(text=script, lang='pt-br')
    audio_file = 'voiceover.mp3'
    tts.save(audio_file)
    return audio_file
