#Este funcion recibe el texto limpio de la url y lo convierte a fichero de audio.mp3
from gtts import gTTS
import os

def text_to_speech_fr(text, pais):
    
    speech = gTTS(text, lang=pais)

    # Save the audio file to a temporary file
    speech_file = 'speech_fr.mp3'
    speech.save(speech_file)
    
    return speech_file