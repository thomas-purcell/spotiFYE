import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "50aed94f72d4414cafa02eda20c45457"
client_secret = "0ce320e6442c4e289b3b35d146f8de17"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://localhost",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


