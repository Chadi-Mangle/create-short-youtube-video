from moviepy.editor import *

def cut_video(name, start, end): 
    clip  = VideoFileClip("video" + ".mp4").subclip(start, end)
    # w, h = clip.size
    # print(w, h)
    clip.write_videofile("video" + "_short.mp4", audio_codec="aac")