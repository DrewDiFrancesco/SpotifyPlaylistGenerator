import pandas as pd
import spotipy
import spotipy.util as util
import random
import requests
import json
import time
from spotipy.oauth2 import SpotifyClientCredentials

class Args:
    def __init__(self,client_id,client_secret,username,playlist_links):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.playlist_links = playlist_links
        redirect_uri = 'http://localhost:7777/callback'
        scope_playlist = 'playlist-modify-public'
        scope_user = 'user-library-modify'
        scope_playing = 'user-read-currently-playing'
        
        #Credentials to access the Spotify Music Data
        manager = SpotifyClientCredentials(client_id,client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=manager)

        #Credentials to access the actual song played
        token_actual = util.prompt_for_user_token(username,scope_playing,client_id,client_secret,redirect_uri) 
        sp_actual = spotipy.Spotify(auth=token_actual)

        #Credentiasl to acces the library music 
        token_user= util.prompt_for_user_token(username,scope_user,client_id,client_secret,redirect_uri) 
        sp_user = spotipy.Spotify(auth=token_user)

        #Credentiasl to acces the Playlists Music
        token_playlist= util.prompt_for_user_token(username,scope_playlist,client_id,client_secret,redirect_uri) 
        sp_playlist = spotipy.Spotify(auth=token_playlist)
    
    @staticmethod
    def create_URI(playlist_link):
        return playlist_link.split("/")[-1].split("?")[0]
        
    def extract_song_features(self):
        playlist_URIs = [self.create_URI(link) for link in self.playlist_links]
        for playlist_uri in playlist_URIs:
            playlist = self.sp.playlist(playlist_uri)
            username = playlist['owner']['id']
            
            track_ids = [playlist['track']['id'] for playlist in self.sp.user_playlist(username, playlist_uri)['tracks']['items']]
            track_features = [self.sp.audio_features(track_id) for track_id in track_ids]
            self.songs.extend(track_features)
       
        

 