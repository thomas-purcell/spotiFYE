from flask import Flask, render_template
import spotipy as spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import spotifye

app = Flask(__name__)

@app.route('/')
def homepage():
    json = spotifye.analyze_user()
    html = render_template('homepage.html', stats=json)
    return html

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)