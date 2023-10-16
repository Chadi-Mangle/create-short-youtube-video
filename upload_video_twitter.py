from ast import Return
from http import client
import tweepy 
import random

##Your api key
bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#api v2 version

def tweet_text(text:str): 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    

    #api.update_status_with_media(text, "video_short.mp4")
    #upload_result = api.media_upload('video_short.mp4')
    api.update_status(status=text)

def tweet_video(videoname:str): 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    text_clear = clear_text(videoname).replace(" - " , " | " )
    #text = text_tweet(text_clear)
    text = text_clear

    #api.update_status_with_media(text, "video_short.mp4")
    upload_result = api.media_upload('video_short.mp4')
    api.update_status(status=text, media_ids=[upload_result.media_id_string])

def featuring(text:str): 

    # print(text)
    text_upper = text.upper()
    text_upper = text_upper.replace("FT","FEAT")
    text_upper = text_upper.replace("FT.","FEAT")
    text_upper = text_upper.replace("FEAT.","FEAT")
    text_upper = text_upper.replace(" X ","FEAT")
    text_upper = text_upper.replace(", @","FEAT")
    
    # print(text_upper)

    if "FEAT" in text_upper: 
        text_list = text_upper.split("FEAT")
        # print(text_list)
        text = text[0:len(text_list[0])]    
        return text, text_list[-1]

    return text, None

def clear_parenthesis(text:str): 
    text = text.replace("[","(")
    text = text.replace("]",")")

    text = text.replace("#","(")

    text = text.replace(" :", "")
    text = text.replace(":", '')

    text = text.replace(")", "")

    if "(" in text:
        text_list = text.split("(")

        # print(text)

        text, featuring_name = featuring(text)
        # print(text, featuring_name)
        if featuring_name: 
            text = if_featuring_name(text, featuring_name)
            # print(text)
        else: 
            text = text_list[0]  

        # print(text_list[0])

        # print(text_list[1])

    text = text.replace("(", "")
    #print(text)
    return text

def clear_text(text:str): 
    text = text.replace("«", "-")
    text = text.replace("»", "")

    text = text.replace('"', "- ", 1)
    text = text.replace('"', "",)

    text = text.replace("//", "-", 1)
    # text = text.replace("/", "-")
    text = text.replace("|", "-")

    text = text.replace("[EXCLU]", "")
    text = text.replace("Clip officiel", "")

    text_upper = text.upper()
    text_upper = text_upper.replace(" FT "," FEAT ")
    text_upper = text_upper.replace("FT.","FEAT")
    text_upper = text_upper.replace("FEAT.","FEAT")

    text = clear_parenthesis(text)
    text, featuring_name = featuring(text)
        # print(text, featuring_name)
    if featuring_name: 
        text = if_featuring_name(text, featuring_name)

    return text 

def if_featuring_name(text:str, featuring_name:str): 
    featuring_name = clear_parenthesis(featuring_name)
    #print(text, featuring_name)
    if '-' in text: # tester: text.replace("-", "Ft. {featuring_name} - ", 1)
        text = text.replace("-", "Ft. {} - ".format(featuring_name.replace(" ", "", 1).capitalize()), 1)
    elif '-' in featuring_name: 
        ft_list = featuring_name.split("-")
        text = text + ' Ft. ' + ft_list[0].replace(" ", "", 1).capitalize() + " - " + ft_list[1].replace(" ", "", 1).capitalize()
    else: 
        text = text + 'Ft. ' + featuring_name.replace(" ", "", 1).capitalize()
        # print(text)
    
    text = text.replace("  ", " ")
    return text

def text_tweet(videoname:str): 
    file = open("text_twitter.txt", "r", encoding="utf-8")
    data = file.read()
    list_text = data.split("\n")
    id = random.randint(0, len(list_text)-1)
    text = list_text[id]
    file.close()
    if "*" in text: 
        if "-" in videoname: 
            if 'Ft.' in videoname: 
                text = list_text[0] 
            else: 
                name = videoname.split("-")
                text_cut = text.split("*")
                text = text_cut[0] + name[0][:-1] + text_cut[1]
        else:
            text = list_text[0]

    if text == list_text[0]:
        text = videoname
    return text