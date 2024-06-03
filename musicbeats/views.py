from django.shortcuts import render
from musicbeats.models import Song

def index(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song': songs})

def songs(request):
    songs = Song.objects.all()
    return render(request, 'musicbeats/songs.html', {'song': songs})

def songpost(request, id):
    songs = Song.objects.filter(song_id=id).first()
    return render(request, 'musicbeats/songpost.html', {'song': songs})

