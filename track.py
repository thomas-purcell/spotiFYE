class Track(object):
    def __init__(self, song, song_id, artists, artists_id, album, album_id, genres, album_cover):
        self.song = song
        self.song_id = song_id
        self.artists = artists
        self.artists_id = artists_id
        self.album = album
        self.album_id = album_id
        self.genres = genres
        self.album_cover = album_cover

    def __repr__(self):
        return [self.song, self.song_id, self.artists, self.artists_id,
                self.album, self.album_id, self.genres, self.album_cover].__str__()

    def __str__(self):
        return [self.song, self.song_id, self.artists, self.artists_id,
                self.album, self.album_id, self.genres, self.album_cover].__str__()
