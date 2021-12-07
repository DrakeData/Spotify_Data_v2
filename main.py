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

results = sp.current_user_recently_played(limit=50, after=None, before=None)

# export json to text file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

json1 = json.dumps(results, indent=4)

a_json = json.loads(json1)
print(a_json['items'][0]['track'])

print(f"Track ID: {a_json['items'][0]['track']['id']}")
print(f"Track Title: {a_json['items'][0]['track']['name']}")
print(f"Album Name: {a_json['items'][0]['track']['album']['name']}")
print(f"Artist Name: {a_json['items'][0]['track']['album']['artists'][0]['name']}")