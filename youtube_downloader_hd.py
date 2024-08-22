import os
from pytube import YouTube
import ffmpeg
from pytube import cipher
import re

def get_throttling_function_name(js: str) -> str:
    """Extract the name of the function that computes the throttling parameter.

    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        The name of the function used to compute the throttling parameter.
    """
    function_patterns = [
        # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
        # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
        # var Bpa = [iha];
        # ...
        # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
        # Bpa.length || iha("")) }};
        # In the above case, `iha` is the relevant function name
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
    ]
    #logger.debug('Finding throttling function name')
    for pattern in function_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(js)
        if function_match:
            #logger.debug("finished regex search, matched: %s", pattern)
            if len(function_match.groups()) == 1:
                return function_match.group(1)
            idx = function_match.group(2)
            if idx:
                idx = idx.strip("[]")
                array = re.search(
                    r'var {nfunc}\s*=\s*(\[.+?\]);'.format(
                        nfunc=re.escape(function_match.group(1))),
                    js
                )
                if array:
                    array = array.group(1).strip("[]").split(",")
                    array = [x.strip() for x in array]
                    return array[int(idx)]

    raise RegexMatchError(
        caller="get_throttling_function_name", pattern="multiple"
    )

cipher.get_throttling_function_name = get_throttling_function_name

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
