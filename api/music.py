import json
import random
import gc

from flask import Response, redirect

path = "resources/"
totalSongSize = 5
songs = json.load( open(path + 'songs.json', 'r') )
playlists = json.load( open(path + 'playlists.json', 'r') )
artists = json.load( open(path + 'artists.json', 'r') )

def getSongTitle(body):
    return songs[ body['id'] ]['t']

def getSongPath( body ):
    # return songs[body['id']]['t'], f"https://www.jiosaavn.com/api.php?__call=song.generateAuthToken&url={songs[body['id']]['emu']}&bitrate={body['b']}&api_version=4&_format=json&ctx=web6dot0&_marker=0"
    return songs[body['id']]['emu']
def getPlaylistSongs( body ):
    temp = dict()
    try:
        currentPlaylist = playlists[ str(body['id']) ]
    except:
        return Response( status=210 )
    temp['t'] = currentPlaylist['t']
    temp['data'] = currentPlaylist['g']
    return temp
# def getPlaylistSongs( body ):
#     temp = dict()
#     try:
#         currentPlaylist = playlists[ str(body['id']) ]
#     except:
#         return Response( status=210 )
#     index = int(body['np'])*totalSongSize                           # npage * limitSize
#     temp['lp'] = index+totalSongSize < len( currentPlaylist['g'] )   # last_page
#     temp['data'] = list( map( songWrapper, currentPlaylist['g'][ index:totalSongSize+index ] ) )
#     return temp

def songWrapper(_id):
    temp = dict()
    temp['id'] = _id
    temp['i'] = songs[_id]['i']
    temp['t'] = songs[_id]['t']
    temp['u'] = songs[_id]['emu']
    return temp

def getImage(type:str, _id:str, size:str):
    if type == "s":
        return redirect( songs[_id]['i'].replace( "50x50", f'{size}x{size}' ) )
    else:
        return redirect( playlists[_id]['i'].replace( "50x50", f'{size}x{size}' ) )
def playlistWrapper(_id):
    temp = dict()
    temp['id'] = _id
    temp['i'] = playlists[_id]['i']
    temp['t'] = playlists[_id]['t']
    return temp
    
def getSampler():
    temp = { 'data':[] }
    for name in [ 'hits', 'latest', 'best' ]:
        keys = random.sample( list(playlists.keys()), 5 )
        temp[name] = keys
    return temp 

playlists_keys_list = list(playlists.keys())

temp = { 'data':[] }
for i, name in enumerate([ 'hits', 'latest', 'best' ]):
    count = i*5
    keys = playlists_keys_list[count:count+5]
    temp[name] = keys
del playlists_keys_list
gc.collect()

def getArranger():
    return temp 