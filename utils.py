def compare(p1, p2):
    titles = {}
    artists = {}
    albums = {}
    genres = {}
    urls = set()
    p1_artists = set()
    p2_artists = set()
    p1_genres = set()
    p2_genres = set()

    for t1 in p1:
        for t2 in p2:
            if t1.song == t2.song:
                if t1.song in titles.keys():
                    titles[t1.song] += 1
                else:
                    titles.update({t1.song: 1})

                if t1.album_cover not in urls:
                    urls.add(t1.album_cover)

                if t2.album_cover not in urls:
                    urls.add(t2.album_cover)

            for artist1 in t1.artists:
                p1_artists.add(artist1)

            for artist2 in t2.artists:
                p2_artists.add(artist2)
                if artist2 in p1_artists:
                    if t1.album_cover not in urls:
                        urls.add(t1.album_cover)

                    if t2.album_cover not in urls:
                        urls.add(t2.album_cover)

            if t1.album == t2.album:

                if t1.album in albums.keys():
                    albums[t1.album] += 1
                else:
                    albums.update({t1.album: 1})

                if t1.album_cover not in urls:
                    urls.add(t1.album_cover)

                if t2.album_cover not in urls:
                    urls.add(t2.album_cover)

            for genre1 in t1.genres:
                p1_genres.add(genre1)

            for genre2 in set(t2.genres):
                p2_genres.add(genre2)

    title_count = 0
    for title in titles.keys():
        title_count += titles[title]

    for artist1 in p1_artists:
        for artist2 in p2_artists:
            if artist1 == artist2:
                if artist1 in artists.keys():
                    artists[artist1] += 1
                else:
                    artists.update({artist1: 1})

    artist_count = 0
    for artist in artists.keys():
        artist_count += artists[artist]

    album_count = 0
    for album in albums.keys():
        album_count += albums[album]

    for genre1 in p1_genres:
        for genre2 in p2_genres:
            if genre1 == genre2:
                if genre1 in genres.keys():
                    genres[genre1] += 1
                else:
                    genres.update({genre1: 1})

    genre_count = 0
    for genre in genres.keys():
        genre_count += genres[genre]

    total_artists = len(p1_artists) + len(p2_artists)
    total_genres = len(p1_genres) + len(p2_genres)
    return title_count, artist_count, total_artists, album_count, genre_count, total_genres, \
        titles, artists, albums, genres, urls


def build_json(title_percent, artist_percent, album_percent, genre_percent, titles, artists, albums, genres, urls):
    result = {"stats": []}
    names = ["Song Similarities", "Artist Similarities", "Album Similarities", "Genre Similarities"]
    percents = [title_percent, artist_percent, album_percent, genre_percent]
    dicts = [titles, artists, albums, genres]
    for idx in range(4):
        stat = {}
        stat.update({"statname": names[idx]})
        stat.update({"percentage": percents[idx]})
        if len(urls) == 0:
            stat.update(
                {"url": "https://cdn.discordapp.com/attachments/812710788476305429/812834007473586196/default.png"})
        elif len(urls) == 1:
            cover = list(urls)
            stat.update({"url": cover[0]})
        else:
            stat.update({"url": urls.pop()})
        strings = []
        for item in dicts[idx].keys():
            strings.append(item)
        stat.update({"strings": strings})
        result['stats'].append(stat)
    return result
