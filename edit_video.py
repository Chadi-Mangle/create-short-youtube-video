from moviepy.editor import *

def cut_video(name, start, end): 
    clip  = VideoFileClip("video" + ".mp4").subclip(start, end)
    clip.write_videofile(name + "_short.mp4", audio_codec="aac")
