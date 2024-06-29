from moviepy.editor import *
import math

# Cargar el audio que deseas agregar al video
clip_name = "Oomph! - Labyrinth"

# Cargar el clip de video de fondo
kermit_with_audio = VideoFileClip('backgrounds/kermit-background (1).mp4')

# Eliminar el audio del clip de video de fondo
kermit = kermit_with_audio.without_audio() # 22 segundos
audio_clip = AudioFileClip(f"clips/{clip_name}.mp3") # mas de 22 segudnos


# Definir el inicio y el final del clip de video de fondo
init = 0 # 0:53 - 1:34
final = audio_clip.duration
duration = final - init



# Ajustar la duración del audio al mismo que el del video
# audio_clip = audio_clip

# Establecer el audio al clip de video de fondo

kermit_loop = concatenate_videoclips([kermit] * (math.ceil(duration / 22))) # 22 segundos que dura el video de kermit

# Combinar los clips de video y texto
final_clip = CompositeVideoClip([kermit_loop])

# Definir la duración del video y escribirlo en un archivo
final_clip.set_audio(audio_clip).set_duration(duration).write_videofile(f"results/{clip_name}_{init}_{final}.mp4", fps=24)

# Cerrar los clips
kermit_with_audio.close()
kermit_loop.close()
final_clip.close()
audio_clip.close()