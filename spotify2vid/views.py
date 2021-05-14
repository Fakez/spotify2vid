import json
import requests
from django.shortcuts import render, redirect
from spotify2vid.classes.SpotifyAuthorizationHandler import SpotifyAuthorizationHandler


def home(request):
    if request.method == 'POST':
        print(request.GET.get('username'))
        return redirect('user_playlists', request.POST.get('username'))
    return render(request, 'home.html')

