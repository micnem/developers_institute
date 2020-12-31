from django.shortcuts import render, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from rest_framework import status
from requests import Request, post
from rest_framework.response import Response
from rest_framework.views import APIView
from .util import *
from api.models import Room
from .models import Artist, TopArtist


class AuthURL(APIView):
    def get(self, request, format=None):
        scopes  = "user-library-read user-top-read playlist-modify-public playlist-modify-private user-read-playback-state user-modify-playback-state user-read-currently-playing"

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)
    
def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')
    print(response.keys())

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    return redirect('frontend:')


class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(
            self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)


class get_top_artists(APIView):
    def get(self, request, format=None):
        room_code = self.request.session.get('room_code')
        room = Room.objects.filter(code=room_code)
        if room.exists():
            room=room[0]
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        host = room.host
        endpoint = "top/artists?time_range=medium_term&limit=30"
        response = execute_spotify_api_request(host, endpoint)

        artist_list = []
        items = response.get('items')

        for item in items:
            spotify_id = item.get('id')
            image = item.get('images')[0].get('url')
            name = item.get('name')
            popularity = item.get('popularity')
            uri = item.get('uri')

            artist = {
                'spotify_id': spotify_id,
                'name': name,
                'image': image,
                'popularity': popularity,
                'uri': uri
            }

            artist_list.append(artist)

        for num, artist in list(enumerate(artist_list[::-1])):
            a, created = Artist.objects.get_or_create(name = artist['name'], spotify_id = artist['spotify_id'], popularity = artist['popularity'], uri = artist['uri'])
            
            ta, created = TopArtist.objects.get_or_create(artist=a, profile=request.user, affinity=num+1)
            
        return Response(artist_list, status=status.HTTP_200_OK)


# class get_related_artists(APIView):
#     def get(self, request, format=None, artist_list):
#         for artist in artist_list:
#             id = artist['spotify_id']
#             endpoint = f"https://api.spotify.com/v1/artists/{id}/related-artists"
#             response = execute_spotify_api_request(endpoint)

#         return Response(artist_list, status=status.HTTP_200_OK)