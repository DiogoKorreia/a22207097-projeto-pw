from bands.models import Band, Musician, Album, Music
import json
from django.db import transaction
from datetime import datetime, timedelta

with open('bands/json/bands.json') as f:
    bands = json.load(f)

    with transaction.atomic():
        for band, info in bands.items():
            print(band, info)

            created_band = Band.objects.create(
                name=band,
                image=info['image'],
                creationDate=info['creationDate']
            )

            for artist_info in info['artists']:
                artist = Musician.objects.create(
                    firstName=artist_info['firstName'],
                    lastName=artist_info['lastName'],
                    instrument=artist_info['instrument'],
                    age=artist_info['age'],
                    band=created_band
                )
                created_band.artists.add(artist)

            for album_info in info['albums']:

                release_date_str = album_info['releaseDate']
                release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()

                album = Album.objects.create(
                    name=album_info['name'],
                    image=album_info['image'],
                    albumLink=album_info['albumLink'],
                    releaseDate=release_date,
                    rating=album_info['rating'],
                    band=created_band
                )

                for music_info in album_info['musics']:
                    duration_str = music_info['duration']
                    duration_parts = [int(part) for part in duration_str.split(':')]
                    duration = timedelta(hours=duration_parts[0], minutes=duration_parts[1], seconds=duration_parts[2])

                    music = Music.objects.create(
                        title=music_info['title'],
                        duration=duration,
                        musicLink=music_info['musicLink'],
                        releaseDate=music_info['releaseDate'],
                        rating=music_info['rating'],
                        album=album
                    )
                    album.musics.add(music)

                created_band.albums.add(album)
