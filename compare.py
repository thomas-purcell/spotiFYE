
def compare(p1, p2):

    title_count = 0
    artist_count = 0
    album_count = 0
    genre_count = 0
    total_genres = 0
    titles = {}
    artists = {}
    albums = {}
    genres = {}

    for t1 in p1:
        total_genres += t1.total_genres
        for t2 in p2:
            if t1.song == t2.song:
                title_count += 1
                if t1.song in titles.keys():
                    titles[t1.song] += 1
                else:
                    titles.update({t1.song: 1})
            if t1.artist == t2.artist:
                artist_count += 1
                if t1.artist in artists.keys():
                    artists[t1.artist] += 1
                else:
                    artists.update({t1.artist: 1})
            if t1.album == t2.album:
                album_count += 1
                if t1.album in albums.keys():
                    albums[t1.album] += 1
                else:
                    albums.update({t1.album: 1})
            for genre in t1.genres:
                if genre in t2.genres:
                    genre_count += 1
                    if genre in genres.keys():
                        genres[genre] += 1
                    else:
                        genres.update({genre: 1})
            total_genres += t2.total_genres

    return title_count, artist_count, album_count, genre_count, total_genres, titles, artists, albums, genres

"""
{ "stats" : [
    { "statname": "song compatibility", 
      "percentage": "10%", 
      "url": "https://albumformostcommonsong",
      "strings": ["list of songs"] 
    },
    { "statname": "artist compatibility", 
      "percentage": "20%", 
      "url": "https://artistphoto",
      "strings": ["list of artists"] 
    },
    { "statname": "album compatibility", 
      "percentage": "15%", 
      "url": "https://albumphoto",
      "strings": ["list of albums"] 
    },
    { "statname": "genre compatibility", 
      "percentage": "10%", 
      "url": "https://?",
      "strings": ["list of genres"] 
    }
    ]
}
"""