from django.db import models
from datetime import timedelta


class Musician (models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=40)
    instrument = models.CharField(max_length=20)
    age = models.IntegerField()
    band = models.ForeignKey('Band', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.firstName} {self.lastName} - {self.age} -{self.instrument} '

class Music(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='bands/images', null=True, blank=True)
    duration = models.DurationField(default=timedelta(minutes=3))
    musicLink = models.URLField(max_length=200,default='')
    releaseDate = models.DateField()
    rating = models.IntegerField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='album_tracks', null=True, default=None)

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'bands/images/2048px-Icon-round-Question_mark.jpg'

    def __str__(self):
        return f'{self.title}'


class Album(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='bands/images', null=True, blank=True)
    albumLink = models.URLField(max_length=200,default='')
    releaseDate = models.DateField()
    rating = models.IntegerField()
    musics = models.ManyToManyField(Music, related_name='albums_included')
    band = models.ForeignKey('Band', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.name} - {self.rating}⭐️'

class Band(models.Model):
    name = models.CharField(max_length=30)
    artists = models.ManyToManyField(Musician, related_name='associated_bands')
    image = models.ImageField(upload_to='bands/images', null=True, blank=True)
    creationDate = models.DateField()
    albums = models.ManyToManyField(Album, related_name='associated_bands_albums')

    def __str__(self):
        return f'{self.name} - {self.artists} : {self.creationDate}'


