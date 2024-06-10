from django.contrib import admin
from .models import Musician, Music, Album, Band

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'instrument', 'age')
    search_fields = ('firstName', 'lastName', 'instrument')

admin.site.register(Musician, MusicianAdmin)

class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'releaseDate', 'rating')
    list_filter = ('releaseDate', 'rating')
    search_fields = ('title','releaseDate')

admin.site.register(Music, MusicAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'releaseDate', 'rating')
    list_filter = ('releaseDate', 'rating')
    search_fields = ('name','releaseDate')

admin.site.register(Album, AlbumAdmin)

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_artists', 'creationDate')
    search_fields = ('name', 'artists__firstName', 'artists__lastName')

    def get_artists(self, obj):
        return ", ".join([artist.firstName for artist in obj.artists.all()])
    get_artists.short_description = 'Artists'

admin.site.register(Band, BandAdmin)
