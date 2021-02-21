import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from track import Track
from utils import compare, build_json


def build_playlist(playlist, sp):
    result = []
    for item in playlist['items']:
        song = item['name']
        song_id = item['uri']
        artists = []
        artists_id = []
        genres = set()
        for artist in item['artists']:
            artists.append(artist['name'])
            artists_id.append(artist['id'])
            genres.update(sp.artist(artist['id'])['genres'])
        album = item['album']['name']
        album_id = item['album']['id']
        album_cover = item['album']['images'][1]['url']
        new_track = Track(song, song_id, artists, artists_id, album, album_id, genres, album_cover)
        result.append(new_track)
    return result


def analyze_user():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.spotify_id,
                                                   client_secret=config.spotify_secret,
                                                   redirect_uri="http://localhost:8080",
                                                   scope="user-read-recently-played, user-top-read"))

    short_playlist = sp.current_user_top_tracks(limit=50, time_range='short_term')
    short_term = build_playlist(short_playlist, sp)

    long_playlist = sp.current_user_top_tracks(limit=50, time_range='long_term')
    long_term = build_playlist(long_playlist, sp)

    title_count, artist_count, total_artists, album_count, genre_count, total_genres, titles, artists, albums, genres, \
        urls = compare(short_term, long_term)

    title_percent = round(title_count / 50 * 100)
    artist_percent = round(artist_count / total_artists * 100)
    album_percent = round(album_count / 50 * 100)
    genre_percent = round(genre_count / total_genres * 100)

    return build_json(title_percent, artist_percent, album_percent, genre_percent,
                      titles, artists, albums, genres, urls)


def main():
    print(analyze_user())


if __name__ == "__main__":
    main()
