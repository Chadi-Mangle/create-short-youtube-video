from yt_dlp import YoutubeDL
import json, requests

def get_video_heatmap(url):
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl: 
        video_info = ydl.extract_info(url, download=False)
        return video_info.get('heatmap')

def most_replay(url:str):
    data = get_video_heatmap(url)
    max_heat_marker_score = 0
    
    for item in data[1:]: 
            heat_marker_score = item["value"]
            if heat_marker_score >= max_heat_marker_score:
                time_in_milisec = item["start_time"]
                max_heat_marker_score = heat_marker_score
    
    return time_in_milisec

def convert_sec_in_h(time_in_sec): 
    time_in_sec = int(time_in_sec)
    time_in_min = int(time_in_sec//60)
    
    if time_in_min//60 > 0: 
        time = str(time_in_min%60).zfill(2) + ':' + str(time_in_min//60).zfill(2) + ':' + str(time_in_sec%60).zfill(2)+'.00'
    else: 
        time = '00:' + str(time_in_min).zfill(2)+ ':' + str(time_in_sec%60).zfill(2)+'.00'

    return time
