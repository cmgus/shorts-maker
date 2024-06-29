from pytube import YouTube
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import numpy as np

def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download(output_path)
    return stream.default_filename

def detect_chorus(video_path):
    path = f"results/{video_path}"
    print(path)
    clip = VideoFileClip(path)
    audio = clip.audio

    recognizer = sr.Recognizer()
    with audio.to_soundarray() as audio_array:
        audio_source = sr.AudioData(np.array(audio_array).tobytes(), clip.audio.fps)
        audio_data = recognizer.record(audio_source)
    
    try:
        chorus = recognizer.recognize_google(audio_data, language="en-US")
        print("Chorus detected: ", chorus)
        return chorus
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def cut_video(video_path, chorus, output_path):
    clip = VideoFileClip(video_path)
    end_time = clip.duration
    start_time = clip.duration - 10  # Extracting last 10 seconds by default
    for i, subclip in enumerate(clip.iter_segments()):
        if chorus in subclip.subclip(0, 10).audio:
            start_time = max(subclip.start, 0)
            break

    final_clip = clip.subclip(start_time, end_time)
    final_clip.write_videofile(output_path)
    print("Video cut successfully")

if __name__ == "__main__":
    # URL del video de YouTube
    video_url = "https://www.youtube.com/watch?v=HR6kOHccYRY"
    
    # Ruta donde se descargará el video
    output_path = "results"
    
    # Descargar el video
    downloaded_video = download_video(video_url, output_path)
    
    # Detectar el coro
    chorus = detect_chorus(downloaded_video)
    
    # Cortar el video en función del coro detectado
    if chorus:
        cut_video(downloaded_video, chorus, "output_cut.mp4")
