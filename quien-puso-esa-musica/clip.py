from moviepy.editor import *

def make_subclip(input_file, output_file, start_time, end_time):
    # Cargar el video original
    audio = AudioFileClip(input_file)
    
    # Definir el rango de tiempo para el subclip
    subclip = audio.subclip(start_time, end_time)
    
    # Guardar el subclip en un nuevo archivo
    subclip.write_audiofile(output_file)

    # Cerrar los clips
    audio.close()
    subclip.close()

name_file = 'Oomph! - Labyrinth'
# Especificar el archivo de entrada
input_file = f'./musics/{name_file}.mp3'

# Especificar el archivo de salida y el rango de tiempo en segundos
output_file = f'./clips/{name_file}.mp3'
start_time = 53  # segundos
end_time = 94    # segundos

# Crear el subclip
make_subclip(input_file, output_file, start_time, end_time)
