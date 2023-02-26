import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

meu_id ='df6b3c9c05294915a408f0e7feaacef0'
minha_chave = 'c0a6cb517dc348ec93c66039ee92ab8c'

client_credentials_manager = SpotifyClientCredentials(client_id=meu_id, client_secret=minha_chave)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

results = sp.artist_top_tracks(lz_uri)


for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])

    print()

