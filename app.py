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
        link = request.form.get('songlink')

        if link_type == 'album':
            results = sp.album(link)
            name = results['name']
            images = results['images']
        elif link_type == 'song':
            results = sp.track(link)
            name = results['album']['name']
            images = results['album']['images']
        else:
            return f"Invalid link or link type. Please try again."

        # return render_template('index.html', name = name, image_url = image_url)
        return render_template('index.html', name = name, images = images)

if __name__ == "__main__":
    app.run(debug=True)