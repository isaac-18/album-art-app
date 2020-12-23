import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

APP_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
APP_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
                                                           client_secret=APP_CLIENT_SECRET))

search_type = int(input("Would like the art from an album (1) or song (2): "))

url = input("Enter the album/song link: ")

if search_type == 1:
    results = sp.album(url)
    item_name = results['name'].replace(' ', '_')
    image_url = results['images'][0]['url']
elif search_type == 2:
    results = sp.track(url)
    item_name = results['name'].replace(' ', '_')
    image_url = results['album']['images'][0]['url']
else:
    print("Error: invalid input")


img_data = requests.get(image_url).content
with open("C:/Users/Isaac/Pictures/album_covers/{}.jpg".format(item_name), 'wb') as handler:
    handler.write(img_data)
