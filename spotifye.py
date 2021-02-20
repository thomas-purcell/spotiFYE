import spotipy
from spotipy.oauth2 import SpotifyOAuth
from track import Track
from compare import compare

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="50aed94f72d4414cafa02eda20c45457",
                                               client_secret="0ce320e6442c4e289b3b35d146f8de17",
                                               redirect_uri="http://localhost:8080",
                                               scope="user-read-recently-played"))


def build_playlist(playlist):
    result = []

    for idx, item in enumerate(playlist['items']):
        track = item['track']
        song = track['name']
        song_id = track['id']
        artist = track['artists'][0]['name']
        artist_id = track['artists'][0]['id']
        album = track['album']['name']
        album_id = track['album']['id']
        genres = sp.artist(artist_id)['genres']
        new_track = Track(song, song_id, artist, artist_id, album, album_id, genres)
        result.append(new_track)

    return result


results = sp.current_user_recently_played(limit=50)
user_playlist = build_playlist(results)  # list of user's last 50 listened to tracks

top_playlists = sp.category_playlists(category_id='toplists', country='us', limit=50)['playlists']
url = top_playlists['items'][0]['external_urls']['spotify']
top_playlist = sp.playlist(url)['tracks']  # top hits playlist from spotify

comparison_playlist = build_playlist(top_playlist)

print(user_playlist)
print(comparison_playlist)

title_count, artist_count, album_count, genre_count, total_genres, titles, artists, albums, genres = compare(user_playlist, comparison_playlist)

print("Song Compatibility: ", str(round(title_count / 50 * 100, 2)), '%')
print("Artist Compatibility: ", str(round(artist_count / 50 * 100, 2)), '%')
print("Album Compatibility: ", str(round(album_count / 50 * 100, 2)), '%')
print("Genre Compatibility: ", str(round(genre_count / total_genres * 100, 2)), '%')
print(titles)
print(artists)
print(albums)
print(genres)
