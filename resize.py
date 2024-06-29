from moviepy.editor import VideoFileClip

def scale_video(input_file, output_file, target_resolution):
    # Cargar el video
    clip = VideoFileClip(input_file)

    # Escalar el video a la resolución objetivo
    scaled_clip = clip.resize(target_resolution)

    # Guardar el video escalado
    scaled_clip.write_videofile(output_file, codec='libx264')

    # Cerrar los clips
    clip.close()
    scaled_clip.close()

# Especificar el archivo de entrada y salida
input_file = 'kermit.mp4'
output_file = 'kermit-high.mp4'

# Especificar la resolución objetivo (ancho x alto)
target_resolution = (1080, 1920)  # Por ejemplo, 1280x720 píxeles

# Escalar el video a la resolución objetivo
scale_video(input_file, output_file, target_resolution)
