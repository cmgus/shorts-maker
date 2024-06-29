from moviepy.editor import *

def make_subclip(input_file, output_file, start_time, end_time):
    # Cargar el video original
    video = VideoFileClip(input_file)
    
    # Definir el rango de tiempo para el subclip
    subclip = video.subclip(start_time, end_time)
    
    # Guardar el subclip en un nuevo archivo
    subclip.write_videofile(output_file, codec='libx264')

    # Cerrar los clips
    video.close()
    subclip.close()

# Especificar el archivo de entrada
input_file = 'subclip2.mp4'

# Especificar el archivo de salida y el rango de tiempo en segundos
output_file = 'subclip3.mp4'
start_time = 0.00  # segundos
end_time = 23.00    # segundos

# Crear el subclip
make_subclip(input_file, output_file, start_time, end_time)
