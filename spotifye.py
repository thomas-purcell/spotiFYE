import spotipy
from spotipy.oauth2 import SpotifyOAuth
from track import Track
from utils import compare, build_json


def build_playlist(playlist, sp):
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
        album_cover = track['album']['images'][1]['url']
        new_track = Track(song, song_id, artist, artist_id, album, album_id, genres, album_cover)
        result.append(new_track)

    return result


def analyze_user():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="50aed94f72d4414cafa02eda20c45457",
                                                   client_secret="0ce320e6442c4e289b3b35d146f8de17",
                                                   redirect_uri="http://localhost:8080",
                                                   scope="user-read-recently-played"))

    results = sp.current_user_recently_played(limit=50)
    user_playlist = build_playlist(results, sp)  # list of user's last 50 listened to tracks

    top_playlists = sp.category_playlists(category_id='toplists', country='us', limit=50)['playlists']
    url = top_playlists['items'][0]['external_urls']['spotify']
    top_playlist = sp.playlist(url)['tracks']  # today's top hits playlist from Spotify

    comparison_playlist = build_playlist(top_playlist, sp)

    title_count, artist_count, album_count, genre_count, total_genres, titles, artists, albums, genres, urls \
        = compare(user_playlist, comparison_playlist)

    title_percent = str(round(title_count / 50 * 100, 2)) + "%"
    artist_percent = str(round(artist_count / 50 * 100, 2)) + "%"
    album_percent = str(round(album_count / 50 * 100, 2)) + "%"
    genre_percent = str(round(genre_count / total_genres * 100, 2)) + "%"

    return build_json(title_percent, artist_percent, album_percent, genre_percent,
                      titles, artists, albums, genres, urls)


def main():
    print(analyze_user())


if __name__ == "__main__":
    main()
