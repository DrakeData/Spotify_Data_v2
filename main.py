import config
import pandas as pd
import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

redirect_uri = 'http://localhost:7777/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id,
                                               client_secret=config.client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-read-recently-played"))

results = sp.current_user_recently_played(limit=50)

# export json to text file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

json1 = json.dumps(results, indent=4)
a_json = json.loads(json1)
print(a_json['items'][0]['track'])


for i in range(len(a_json)):
    print(f"Track ID: {a_json['items'][i]['track']['id']}")
    print(f"Track Title: {a_json['items'][i]['track']['name']}")
    print(f"Album Name: {a_json['items'][i]['track']['album']['name']}")
    for x in range(len(a_json['items'][i]['track']['album']['artists'])):
        print(f"Artist Name: {a_json['items'][i]['track']['artists'][x]['name']}")


## Get Playlist information

results2 = sp.playlist('0OwZcV6bAN2jqqXmA23Jnw?si=7e0fd30e5bd44bfa', fields=None, market=None, additional_types=('track', ))
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(results2, f, ensure_ascii=False, indent=4)


json2 = json.dumps(results2, indent=4)
b_json = json.loads(json2)
print(len(b_json['tracks']['items']))


for i in range(len(b_json['tracks']['items'])):
    print(f"Track Name: {b_json['tracks']['items'][i]['track']['name']}")
    print(f"Track ID: {b_json['tracks']['items'][i]['track']['id']}")

