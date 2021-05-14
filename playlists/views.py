import json
import requests
from django.shortcuts import render
from django.http import JsonResponse

from spotify2vid.classes.SpotifyAuthorizationHandler import SpotifyAuthorizationHandler
from spotify2vid.classes.YoutubeHandler import YoutubeHandler


def user_playlists_view(request, user_id):
    access_token = SpotifyAuthorizationHandler().refreshToken()

    url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    params = {
        'user_id': user_id,
    }

    response = requests.get(url, headers=headers, params=params)
    user_playlists = json.loads(response.text)

    return render(request, 'user_playlists_view.html', {'data': user_playlists,'user_id': user_id})

def single_playlist_view(request, user_id, playlist_id):
    # f = open("response2.txt", "r")
    # playlist_data = json.load(f)

    access_token = SpotifyAuthorizationHandler().refreshToken()

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    params = {
        'fields': """items(track(name,href,duration_ms,album(name,href,images(url)),artists(name,href))),limit,next,offset,previous,total"""
    }

    response = requests.get(url, headers=headers, params=params)
    playlist_data = json.loads(response.text)


    return render(request, 'single_playlist_view.html', {'data': playlist_data})

def yt_search(request, song_info):
    return JsonResponse( {'video_id': YoutubeHandler().youtubesearchpython(song_info)} )



