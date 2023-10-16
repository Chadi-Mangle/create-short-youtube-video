import os
import youtube_downloader_hd
from time import time
import ffmpeg
from pytube import YouTube, Playlist
import json, requests
import best_moment_in_video, edit_video

url = "https://youtu.be/_A9edHn1pN8"


if best_moment_in_video.most_replay(url) == 0: 
    quit()
else: 
    os.remove("video.mp4")
    os.remove("video_short.mp4")

# print(url)
# def delete_video_from_playlist(playlist_url): 

youtube_video = YouTube(url)
# print(youtube_video.video_id)


youtube_downloader_hd.download_video(url)
youtube_video = YouTube(url)


best_moment_time = best_moment_in_video.most_replay(url)
timeur = best_moment_in_video.convert_mili_in_h(best_moment_time)
print(f'Le meilleur moment de la vidéo: "{youtube_video.title}" se trouve à {timeur}')

videoname = youtube_video.title
subclip_start = best_moment_time//1000
subclip_end = (best_moment_time+ 30000)//1000 

edit_video.cut_video(videoname,subclip_start,subclip_end)   
# print("oui") 
