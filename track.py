class Track(object):
    def __init__(self, song, song_id, artist, artist_id, album, album_id, genres, album_cover):
        self.song = song
        self.song_id = song_id
        self.artist = artist
        self.artist_id = artist_id
        self.album = album
        self.album_id = album_id
        self.genres = genres
        self.total_genres = len(genres)
        self.album_cover = album_cover

    def __repr__(self):
        return [self.song, self.song_id, self.artist, self.artist_id,
                self.album, self.album_id, self.genres, self.album_cover].__str__()

    def __str__(self):
        return [self.song, self.song_id, self.artist, self.artist_id,
                self.album, self.album_id, self.genres, self.album_cover].__str__()
