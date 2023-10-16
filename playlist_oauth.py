import os 
import pickle
from urllib import request, response
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

credentials = None

# token.pickle stores the user's credentials from previously successful logins
if os.path.exists('token.pickle'):
    print('Chargment des identifiants...')
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

# If there are no valid credentials available, then either refresh the token or log in.
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Tokens...')
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=[
                "https://www.googleapis.com/auth/youtube.force-ssl"
            ]
        )

        flow.run_local_server(port=8080, prompt='consent',
                              authorization_prompt_message='')
        credentials = flow.credentials

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)

def delete_first_elem(playlist_id): 
    youtube = build("youtube", "v3", credentials=credentials)

    request = youtube.playlistItems().list(
        part="status, contentDetails", playlistId=playlist_id
    )

    response = request.execute()

    # for item in response['items']: 
    #     vid_id = item["id"]


    vid_id = response['items'][0]["id"]
    # print(vid_id)

    request = youtube.playlistItems().delete(
        id=vid_id
    )
    response = request.execute()

    print(response)

# delete_first_elem("PLzFEhfPxC4TqSPhIbp5lmqvzZ1lzGi5wE")