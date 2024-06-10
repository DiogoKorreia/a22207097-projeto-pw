from django import forms
from .models import Musician, Music, Album, Band

class MusicianForm(forms.ModelForm):
  class Meta:
    model = Musician
    fields = '__all__'

class MusicForm(forms.ModelForm):
  class Meta:
    model = Music
    fields = '__all__'

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

class BandForm(forms.ModelForm):
  class Meta:
    model = Band
    fields = '__all__'

    widgets = {
      'name': forms.TextInput(attrs={
          'placeholder':'Band Name',
      })
    }

    labels = {
      'creationDate': 'Creation Date',
    }