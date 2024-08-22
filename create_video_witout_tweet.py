import os, shutil
from time import time
import ffmpeg
from pytube import YouTube, Playlist
import json, requests
import best_moment_in_video, edit_video
import youtube_downloader_hd

url = os.getenv("URL")

if best_moment_in_video.most_replay(url) == 0: 
    quit()
#else: 
    #os.remove("video.mp4")
    #os.remove("video_short.mp4")

# def delete_video_from_playlist(playlist_url): 

youtube_downloader_hd.download_video(url)
youtube_video = YouTube(url)

best_moment_time = best_moment_in_video.most_replay(url)
timeur = best_moment_in_video.convert_sec_in_h(best_moment_time)
print(f'Le meilleur moment de la vidéo: "{youtube_video.title}" se trouve à {timeur}')

videoname = youtube_video.title
subclip_start = best_moment_time
subclip_end = best_moment_time+ 30

edit_video.cut_video(videoname,subclip_start,subclip_end)   
shutil.move("./" + videoname + "_short.mp4", "/tmp/" + videoname + "_short.mp4")
print("End")  
