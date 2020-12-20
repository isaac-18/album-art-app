import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

APP_CLIENT_ID = ""
APP_CLIENT_SECRET = ""

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
                                                           client_secret=APP_CLIENT_SECRET))

album_url = 'https://open.spotify.com/album/10D2HYrLcMJj2QPJt02Adq?si=Uzu3DbwPSNCvD4am9mBUbw'
results = sp.album(album_url)

album_name = results['name'].replace(' ', '_')
image_url = results['images'][0]['url']

img_data = requests.get(image_url).content
with open("C:/Users/Isaac/Pictures/album_covers/{}.jpg".format(album_name), 'wb') as handler:
    handler.write(img_data)
