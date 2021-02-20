import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from track import Track


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="50aed94f72d4414cafa02eda20c45457",
                                               client_secret="0ce320e6442c4e289b3b35d146f8de17",
                                               redirect_uri="http://localhost:8080",
                                               scope="user-read-recently-played"))

results = sp.current_user_recently_played()
user_playlist = []  # list of user's last 50 listened to tracks

for idx, item in enumerate(results['items']):
    track = item['track']
    song = track['name']
    song_id = track['id']
    artist = track['artists'][0]['name']
    artist_id = track['artists'][0]['id']
    album = track['album']['name']
    album_id = track['album']['id']
    new_track = Track(song, song_id, artist, artist_id, album, album_id)
    user_playlist.append(new_track)

playlists = sp.category_playlists(category_id='toplists', country='us', limit=50)['playlists']
url = playlists['items'][0]['external_urls']['spotify']
top_hits_playlist = sp.playlist(url)['tracks']['items']  # top hits playlist from spotify

comparison_playlist = []
for idx, item in enumerate(top_hits_playlist):
    track = item['track']
    song = track['name']
    song_id = track['id']
    artist = track['artists'][0]['name']
    artist_id = track['artists'][0]['id']
    album = track['album']['name']
    album_id = track['album']['id']
    new_track = Track(song, song_id, artist, artist_id, album, album_id)
    comparison_playlist.append(new_track)

print(user_playlist)
print(comparison_playlist)


# compare(user_playlist, top_hits_playlist)
