from django.shortcuts import render, redirect, get_object_or_404
from .models import Band, Album, Music, Musician
from .forms import MusicianForm, MusicForm, AlbumForm, BandForm
from .decorators import group_required


def bandsList_view(request):
    bands = Band.objects.all()
    context = {'bands': bands.order_by('name')}
    return render(request,"bands/bandsList.html",context)

def bandAlbums_view(request, band_id):

    band = get_object_or_404(Band, id=band_id)
    albums = Album.objects.filter(band=band)

    context = {
        'band': band,
        'albums': albums.order_by('releaseDate'),
        }

    return render(request,"bands/bandAlbums.html", context)

def album_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    band = album.band
    context = {
        'album':album,
        'band':band,
        }

    return render(request,"bands/album.html", context)

def music_view(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    context = {'music': music}

    return render(request,"bands/music.html", context)



@group_required('editores de bandas')
def new_musician_view(request):

    form = MusicianForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bands:user_view')

    context = {'form': form}
    return render(request, 'bands/newMusician.html', context)

@group_required('editores de bandas')
def edit_musician_view(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)

    if request.POST:
        form = MusicianForm(request.POST or None, request.FILES, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('bands:user_view')
    else:
        form = MusicianForm(instance=musician)

    context = {'form': form, 'musician':musician}
    return render(request, 'bands/editMusician.html', context)

@group_required('editores de bandas')
def delete_musician_view(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    musician.delete()
    return redirect('bands:user_view')



@group_required('editores de bandas')
def new_music_view(request):

    form = MusicForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bands:user_view')

    context = {'form': form}
    return render(request, 'bands/newMusic.html', context)

@group_required('editores de bandas')
def edit_music_view(request, music_id):
    music = get_object_or_404(Music, id=music_id)

    if request.POST:
        form = MusicForm(request.POST or None, request.FILES, instance=music)
        if form.is_valid():
            form.save()
            return redirect('bands:user_view')
    else:
        form = MusicForm(instance=music)

    context = {'form': form, 'music':music}
    return render(request, 'bands/editMusic.html', context)

@group_required('editores de bandas')
def delete_music_view(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    music.delete()
    return redirect('bands:user_view')



@group_required('editores de bandas')
def new_album_view(request):

    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bands:user_view')

    context = {'form': form}
    return render(request, 'bands/newAlbum.html', context)

@group_required('editores de bandas')
def edit_album_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bands:user_view')
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album':album}
    return render(request, 'bands/editAlbum.html', context)

@group_required('editores de bandas')
def delete_album_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    album.delete()
    return redirect('bands:user_view')



@group_required('editores de bandas')
def new_band_view(request):

    form = BandForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bands:user_view')

    context = {'form': form}
    return render(request, 'bands/newBand.html', context)

@group_required('editores de bandas')
def edit_band_view(request, band_id):
    band = get_object_or_404(Band, id=band_id)

    if request.POST:
        form = BandForm(request.POST or None, request.FILES, instance=band)
        if form.is_valid():
            form.save()
            return redirect('bands:user_view')
    else:
        form = BandForm(instance=band)

    context = {'form': form, 'band':band}
    return render(request, 'bands/editBand.html', context)

@group_required('editores de bandas')
def delete_band_view(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    band.delete()
    return redirect('bands:user_view')





