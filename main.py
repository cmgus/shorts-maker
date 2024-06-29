from moviepy.editor import *
  
# Cargar la imagen de fondo
background_image = ImageClip('backgrounds/final-back.jpg')

init = 74.3
final = 92.91
duration = final - init

# Texto a mostrar en el video
txt = """
Necesito un amor\n
Alguien que por favor\n
Que me cuide y me abracé\n
Que me de su calor\n
Que me quite el dolor\n
Que me ayude a arrancarte\n
Necesito un amor\n
Alguien que por favor\n
Que me ayude a olvidarte\n
"""
clip_name = f"Necesito un amor"
#  Crear el clip de texto
text_clip = (TextClip(txt, color='#E7EE4F', fontsize=40, font='Xolonium-Bold')
             .set_audio(AudioFileClip(f"musics/{clip_name}.mp3").subclip(init, final))
             .set_position('center')
             .set_duration(duration))
text_clip_copy_top = (TextClip("@_ta7u7", color='white', fontsize=40, font='Cantarell-Bold')
             .set_position((470, 300))
             .set_duration(duration))


# Combinar la imagen de fondo con el clip de texto

final_clip = CompositeVideoClip([background_image, text_clip, text_clip_copy_top])

# Establecer el audio al clip
# final_clip_with_audio = final_clip.set_audio(AudioFileClip('esperon-daño.mp3').subclip(init, final))

# Definir la duración del video y escribirlo en un archivo
final_clip.set_duration(duration).write_videofile(f"results/{clip_name}_{init}_{final}.mp4", fps=1)

