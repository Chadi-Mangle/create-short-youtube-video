from pytube import YouTube
import json, requests

def most_replay(url:str):
    youtube_video = YouTube(url)

    mostReplayed = "https://yt.lemnoslife.com/videos?part=mostReplayed&id=" + youtube_video.video_id 
    response = requests.get(mostReplayed)
    text = response.text
    data = json.loads(text)
    
    max_heat_marker_score = 0
    #print(json.dumps(data, sort_keys=True, indent=4))

    try: 
        for items in (data["items"][0]["mostReplayed"]["heatMarkers"]): 
            heat_marker_score = items["heatMarkerRenderer"]["heatMarkerIntensityScoreNormalized"]
            if heat_marker_score >= max_heat_marker_score: 
                time_in_millisec = items["heatMarkerRenderer"]["timeRangeStartMillis"]
                max_heat_marker_score = heat_marker_score
                if time_in_millisec == 0: 
                    max_heat_marker_score = 0
        
        return time_in_millisec
    except KeyError:
        print("\n"'\033[91m' + data["error"]["message"]+ '\033[0m'"\n")  
        return 0
    except: #Retravaillez l'exepsion
        print("Information is not available regarding this video.")
        return 0


def convert_mili_in_h(time_in_millisec): 
    time_in_sec = int(time_in_millisec/1000)
    # time_in_sec = 3601

    # print(time_in_sec)
    time_in_min = time_in_sec//60
    # print(time_in_min)
    if time_in_min//60 > 0: 
        time = str(time_in_min%60).zfill(2) + ':' + str(time_in_min//60).zfill(2) + ':' + str(time_in_sec%60).zfill(2)+'.00'
        print("oui")
    else: 
        time = '00:' + str(time_in_min).zfill(2)+ ':' + str(time_in_sec%60).zfill(2)+'.00'


    return time

#print(most_replay("https://youtu.be/e5t5eW8_CKY?list=RDD04KoPalXlA"))
