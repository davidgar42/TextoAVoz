#Función principal
#Solicita la url donde esta alojado el articulo para convertirlo a audio mp3
#imports
from getTexto import getText
from getTrack import text_to_speech
from playsound import playsound  # para reproducir el archivo mp3 generado


#url = 'https://edition.cnn.com/2023/06/10/sport/manchester-city-wins-champions-league-for-first-time-beating-inter-milan-1-0-in-tense-istanbul-final/index.html'
#url = 'https://learnenglish.britishcouncil.org/general-english/magazine-zone/world-tourism-day'
url = 'https://gtts.readthedocs.io/en/latest/cli.html#cmdoption-gtts-cli-o'

text = getText(url)
print(text)
track = text_to_speech(text)


playsound(track)