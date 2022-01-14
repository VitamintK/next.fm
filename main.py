# import requests
import requests_cache
import time
from collections import defaultdict
try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda f: f

with open('api_key.txt', 'r') as f:
    APIKEY = f.read().strip()

session = requests_cache.CachedSession('http_cache', backend='filesystem')
URLBASE = 'http://ws.audioscrobbler.com/2.0/'
def get_all_tracks(api_key, user):
    # gettoptracks returns all tracks, with a duration for each track, but does NOT supply the corresponding album.
    # getrecenttracks returns all tracks, with the album for each track, but does NOT supply the duration.
    # we'll exhaustively go through BOTH calls, and join them using the "URL" as a unique identifier.

    # first, gettoptracks
    DEFAULTDURATION = 100
    METHOD = 'user.gettoptracks'
    LIMIT=1000 # maximum page size
    url = f'{URLBASE}?method={METHOD}&user={user}&api_key={api_key}&format=json&limit={LIMIT}'
    r = session.get(url)
    j = r.json()
    num_pages = int(j['toptracks']['@attr']['totalPages'])
    track_accumulator = dict()
    for page in tqdm(range(1,num_pages+1)):
        url = f'{URLBASE}?method={METHOD}&user={user}&api_key={api_key}&format=json&limit={LIMIT}&page={page}'
        r = session.get(url)
        j = r.json()
        tracks = j['toptracks']['track']
        for track in tracks:
            uid = track['url']
            assert uid not in track_accumulator, uid
            track_accumulator[uid] = track
        time.sleep(0.15)
    
    # second, getrecenttracks
    LIMIT=1000 # maximum page size
    METHOD = 'user.getrecenttracks'
    url = f'{URLBASE}?method={METHOD}&user={user}&api_key={api_key}&format=json&limit={LIMIT}'
    r = session.get(url)
    j = r.json()
    num_pages = int(j['recenttracks']['@attr']['totalPages'])
    for page in tqdm(range(1,num_pages+1)):
        url = f'{URLBASE}?method={METHOD}&user={user}&api_key={api_key}&format=json&limit={LIMIT}&page={page}'
        r = session.get(url)
        j = r.json()
        tracks = j['recenttracks']['track']
        for track in tracks:
            uid = track['url']
            track_accumulator[uid]['album'] = track['album']
        time.sleep(0.15)
    
    album_accumulator = defaultdict(int)
    for track in track_accumulator.values():
        if track['duration']=='0':
            print(f'no duration! setting duration to default {DEFAULTDURATION}')
            print(track)
            duration = DEFAULTDURATION
        else:
            duration = int(track['duration'])
        album_accumulator[track['album']['#text']] += duration * int(track['playcount'])
    
    results = list(album_accumulator.items())
    results.sort(key=lambda x: -x[1])
    for album,seconds in results:
        if seconds/3600 < 3:
            break
        print(album, seconds) 

get_all_tracks(APIKEY, 'vitamintk')
