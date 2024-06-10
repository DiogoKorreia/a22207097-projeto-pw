from django.urls import path
from .views import bandsList_view, bandAlbums_view, album_view, music_view, new_musician_view, new_music_view, new_album_view, new_band_view,edit_musician_view, edit_music_view, edit_album_view, edit_band_view, delete_music_view, delete_album_view, delete_band_view


app_name = 'bands'

urlpatterns = [
    path('', bandsList_view, name='bands_list'),
    path('<int:band_id>/', bandAlbums_view, name='band_albums'),
    path('albums/<int:album_id>/', album_view, name='album_details'),
    path('music/<int:music_id>/', music_view, name='music_details'),
    path('user/newMusician',new_musician_view,name='new_musician'),
    path('user/newMusic',new_music_view,name='new_music'),
    path('user/newAlbum',new_album_view,name='new_album'),
    path('user/newBand',new_band_view,name='new_band'),
    path('user/editMusician/<int:musician_id>',edit_musician_view,name='edit_musician'),
    path('user/editMusic/<int:music_id>',edit_music_view,name='edit_music'),
    path('user/editAlbum/<int:album_id>',edit_album_view,name='edit_album'),
    path('user/editBand/<int:band_id>',edit_band_view,name='edit_band'),
    path('music/<int:music_id>/delete', delete_music_view,name="delete_music"),
    path('albums/<int:album_id>/delete', delete_album_view,name="delete_album"),
    path('<int:band_id>/delete', delete_band_view,name="delete_band"),
]