import random


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
    urls = set()

    for t1 in p1:
        total_genres += t1.total_genres
        for t2 in p2:
            if t1.song == t2.song:
                title_count += 1
                if t1.song in titles.keys():
                    titles[t1.song] += 1
                else:
                    titles.update({t1.song: 1})
                if t1.album_cover not in urls:
                    urls.add(t1.album_cover)
                if t2.album_cover not in urls:
                    urls.add(t2.album_cover)
            if t1.artist == t2.artist:
                artist_count += 1
                if t1.artist in artists.keys():
                    artists[t1.artist] += 1
                else:
                    artists.update({t1.artist: 1})
                if t1.album_cover not in urls:
                    urls.add(t1.album_cover)
                if t2.album_cover not in urls:
                    urls.add(t2.album_cover)
            if t1.album == t2.album:
                album_count += 1
                if t1.album in albums.keys():
                    albums[t1.album] += 1
                else:
                    albums.update({t1.album: 1})
                if t1.album_cover not in urls:
                    urls.add(t1.album_cover)
                if t2.album_cover not in urls:
                    urls.add(t2.album_cover)
            for genre in t1.genres:
                if genre in t2.genres:
                    genre_count += 1
                    if genre in genres.keys():
                        genres[genre] += 1
                    else:
                        genres.update({genre: 1})
            total_genres += t2.total_genres

    return title_count, artist_count, album_count, genre_count, total_genres, titles, artists, albums, genres, urls


def build_json(title_percent, artist_percent, album_percent, genre_percent, titles, artists, albums, genres, urls):
    result = "{ \"stats\": ["
    names = ["Song Similarities", "Artist Similarities", "Album Similarities", "Genre Similarities"]
    percents = [title_percent, artist_percent, album_percent, genre_percent]
    dicts = [titles, artists, albums, genres]
    for idx in range(4):
        result += "{ \"statname\": \"" + names[idx] + "\", "
        result += "\"percentage\": \"" + percents[idx] + "\", "
        if len(urls) == 0:
            result += "\"url\": \"" + \
                      "https://cdn.discordapp.com/attachments/812710788476305429/812834007473586196/default.png" \
                      + "\", "
        elif len(urls) == 1:
            cover = list(urls)
            result += "\"url\": \"" + cover[0] + "\", "
        else:
            result += "\"url\": \"" + urls.pop() + "\", "
        strings = "["
        for item in dicts[idx].keys():
            strings += "\"" + item + "\", "
        strings = strings[0:len(strings) - 2] + "] "
        result += "\"strings\": " + strings
        result += "}, "
    return result[0:len(result) - 2] + " ] }"
