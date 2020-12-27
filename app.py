import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, request

APP_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
APP_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
                                                            client_secret=APP_CLIENT_SECRET))

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        # form_data = request.form
        # return render_template('data.html',form_data = form_data)
        
        link_type = request.form.get('link_type')
        link = request.form.get('link')

        if link_type == 'album':
            results = sp.album(link)
            name = results['name']
            image_url = results['images'][0]['url']
        elif link_type == 'song':
            results = sp.track(link)
            name = results['name']
            image_url = results['album']['images'][0]['url']

        return render_template('index.html', name = name, image_url = image_url)

# class AlbumSongObj:
#     APP_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
#     APP_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

#     sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
#                                                             client_secret=APP_CLIENT_SECRET))
    
#     def __init__(self, link, itemType):
#         self.link = link
#         self.itemType = itemType
#         self.imageURL
#         self.name

#     def get_image_url():
#         if itemType == 'album':
#             results = sp.album(link)
#             name = results['name']
#             image_url = results['images'][0]['url']
#         elif itemType == 'song':
#             results = sp.track(url)
#             name = results['name']
#             image_url = results['album']['images'][0]['url']


if __name__ == "__main__":
    app.run(debug=True)