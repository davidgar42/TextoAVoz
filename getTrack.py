#Este funcion recibe el texto limpio de la url y lo convierte a fichero de audio.mp3
from gtts import gTTS
import os

pais = 'es'
def text_to_speech(text, pais):
    
    speech = gTTS(text, lang=pais, tld='es')

    # Save the audio file to a temporary file
    speech_file = 'speech_es.mp3'
    speech.save(speech_file)
    
    return speech_file
    





# def text_to_speech(text):
#     # Initialize gTTS with the text to convert
#     speech = gTTS(text)

#     # Save the audio file to a temporary file
#     speech_file = 'speech.mp3'
#     speech.save(speech_file)


#     return speech_file