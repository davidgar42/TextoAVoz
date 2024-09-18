#Función principal
#Solicita la url donde esta alojado el articulo para convertirlo a audio mp3
#imports
from getTexto import getText
from getTrack_es import text_to_speech_es
from getTrack_eng import text_to_speech_eng
from getTrack_fr import text_to_speech_fr
from playsound import playsound  # para reproducir el archivo mp3 generado


#url = 'https://edition.cnn.com/2023/06/10/sport/manchester-city-wins-champions-league-for-first-time-beating-inter-milan-1-0-in-tense-istanbul-final/index.html'
#url = 'https://learnenglish.britishcouncil.org/general-english/magazine-zone/world-tourism-day'
#url = 'https://www.elespanol.com/invertia/opinion/20240907/inclusion-financiera-progresa-adecuadamente/884031598_12.html'

# Solicitando datos al usuario
print(f"*****Bienvenido al convertidor de articulos a audio mp3******\n")
url = input("Pega la URL donde esta el articulo a convertir: ")
pais = input("\nIntroduce 'es' para Español, 'en' para ingles o 'fr' para frances: ")

# Enviando la dirección url a la funcion getText()
text = getText(url)

#Envio del lenguaje a gtts para transcribir correctamente el audio

if pais == 'es':
    track = text_to_speech_es(text, pais)
elif pais == 'en':
    track = text_to_speech_eng(text, pais)
elif pais == 'fr':
    track = text_to_speech_fr(text, pais)
else:
    print("Valor por defecto 'es'")
    track = text_to_speech_es(text, 'es')

#playsound(track)