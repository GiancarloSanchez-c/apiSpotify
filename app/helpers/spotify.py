from os import getenv
from requests import post, get
from base64 import b64encode

AUTH_ENDPOINT='https://accounts.spotify.com/api/token'
AUTH_SEARCH_ENDOPOINT='https://api.spotify.com/v1/search'
AUTH_GET_ARTIST_ENDPOINT='https://api.spotify.com/v1/artists/{id}'
AUTH_GET_RELATED_ARTIST_ENDPOINT='https://api.spotify.com/v1/artists/{id}/related-artists'
AUTH_GET_ARTIST_TRACK = 'https://api.spotify.com/v1/artists/{id}/top-tracks'

def auth_token():
    
    client_id = getenv('SPOTIFY_CLIENT_ID')
    client_secret = getenv('SPOTIFY_CLIENT_SECRET')
    
    # Authorization BASE64
    
    auth_client=f'{client_id}:{client_secret}'
    
    #CODIFICA EL TOKEN
    message = auth_client.encode('ascii')
    #LEE EL MENSAJE CODIFICADO
    bs64encode = b64encode(message)
    #LEE EL MENSAJE DECODIFICADO 
    b64_token = bs64encode.decode('ascii')
    
    headers = {
        'Authorization' : f'Basic {b64_token}'
    }
    
    data = {
        'grant_type' : 'client_credentials'
    }
    
    response = post(AUTH_ENDPOINT, headers=headers, data=data)
    return (response.json())['access_token']

#BUSCAR ARTISTA POR NOMBRE
def search_artist_name(name):
    params = {
        'q': name,
        'type': 'artist',
    }
    
    token=auth_token()
    
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    
    response = get(AUTH_SEARCH_ENDOPOINT, params=params, headers=headers)
    return response.json()

def get_artist(artist_id):
    
    url = AUTH_GET_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    
    response = get(url, headers=headers)
    
    return response.json()

def get_artist_related(artist_id):
    url = AUTH_GET_RELATED_ARTIST_ENDPOINT.format(id=artist_id)
    token = auth_token()
    
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    
    response = get(url, headers=headers)
    
    return response.json()


def get_artist_track(artist_id):
    url = AUTH_GET_ARTIST_TRACK.format(id=artist_id)
    token = auth_token()
    
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    
    params = {
        'market' : 'US'
    }
    response = get(url, params=params, headers=headers)
    
    return response.json()