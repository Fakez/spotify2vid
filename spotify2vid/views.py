import json
import requests
from django.shortcuts import render, redirect


def home(request):
    if request.method == 'POST':
        print(request.GET.get('username'))
        return redirect('user_playlists', request.POST.get('username'))
    return render(request, 'home.html')

