from moviepy.editor import VideoFileClip

def get_video_resolution(video_path):
    # Cargar el video
    clip = VideoFileClip(video_path)

    # Obtener la resolución del video
    resolution = clip.size

    # Cerrar el clip
    clip.close()

    return resolution

# Especifica la ruta del archivo de video
video_path = 'kermit-background.mp4'

# Obtiene la resolución del video
resolution = get_video_resolution(video_path)

# print("Resolución del video:", resolution[0])



# from moviepy.editor import VideoFileClip

def crop_video(input_file, output_file, x1, y1, x2, y2):
    # Load the video clip
    clip = VideoFileClip(input_file)

    # Calculate the new dimensions
    width = x2 - x1
    height = y2 - y1

    # Crop the video
    cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

    # Save the cropped video
    cropped_clip.write_videofile(output_file, codec='libx264')

    # Close the clips
    clip.close()
    cropped_clip.close()

# Specify input and output file paths
input_file = 'kermit-background.mp4'
output_file = 'kermit.mp4'

# Specify crop coordinates (x1, y1) to (x2, y2)
x1 = (resolution[0]/8)*4  # starting x coordinate for cropping
y1 = 0   # starting y coordinate for cropping
x2 = (resolution[0]/8)*6  # ending x coordinate for cropping
y2 = 1080  # ending y coordinate for cropping

# Crop the video
crop_video(input_file, output_file, x1, y1, x2, y2)