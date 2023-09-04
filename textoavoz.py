from gtts import gTTS
import os

def crear_audio_desde_texto(texto, nombre_archivo):
    try:
        # Crear un objeto gTTS con el texto y el idioma 'es' (español)
        tts = gTTS(text=texto, lang='es')

        # Guardar el archivo de audio en formato MP3 con el nombre especificado
        tts.save(nombre_archivo)
        print(f"Archivo de audio '{nombre_archivo}' creado con éxito.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    texto_ingresado = input("Ingresa el texto que deseas convertir en audio: ")
    nombre_archivo = input("Ingresa el nombre del archivo de audio (sin extensión): ") + ".mp3"

    crear_audio_desde_texto(texto_ingresado, nombre_archivo)
