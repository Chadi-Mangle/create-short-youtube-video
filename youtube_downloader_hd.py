import os
from pytube import YouTube
import ffmpeg

def on_download_progress(stream, chunk, bytes_remaining): 

    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Progression du téléchargement:{int(percent)}%")
    
def download_video(url): 

    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress)

    # print("Titre: ", youtube_video.title)
    #print("Vues: ", youtube_video.views)

    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='video',).order_by('resolution').desc()
    
    # for stream in streams: 
    #   print(stream)


    for stream in streams: 
        if int(stream.resolution[0:len(stream.resolution) -1]) < 1080: 
            video_stream = stream
            break
    
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='audio',).order_by('abr').desc()
    audio_stream = streams[0] #0
    

    # print(f"Vidéo : {video_stream}")
    # print(f"Audio : {audio_stream}")


    print(f"Telechargment de {youtube_video.title}...")
    

    video_stream.download("video")
    audio_stream.download("audio")
    audio_filename = os.path.join("audio", video_stream.default_filename)
    video_filename = os.path.join("video", video_stream.default_filename)
    output_filename = video_stream.default_filename

    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)

    print("La vidéo à bien été téléchargé")


    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")

    os.rename(output_filename, "video.mp4")
