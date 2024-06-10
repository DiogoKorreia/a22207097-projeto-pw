from bands.models import Band, Album

from django.db import transaction

@transaction.atomic
def connect_artists_to_band():
    print('artists')
    bands = Band.objects.all()
    for band in bands:
        artists = band.artists.all()
        artists.update(band=band)

@transaction.atomic
def connect_albums_to_band():
    print('albums')
    bands = Band.objects.all()
    for band in bands:
        albums = band.albums.all()
        albums.update(band=band)

@transaction.atomic
def connect_music_to_albums():
    print('musics')
    albums = Album.objects.all()
    for album in albums:
        musics = album.musics.all()
        musics.update(album=album)

if __name__ == "__main__":
    connect_artists_to_band()
    connect_albums_to_band()
    connect_music_to_albums()
