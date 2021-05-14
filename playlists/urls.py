
from django.urls import path
from . import views


urlpatterns = [
    path('',views.user_playlists_view),
    path('<str:user_id>', views.user_playlists_view, name='user_playlists'),
    path('<str:user_id>/<str:playlist_id>', views.single_playlist_view, name='playlist_details'),
    path('api/search/<str:song_info>', views.yt_search),
    
]
