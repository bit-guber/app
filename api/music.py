import json
import random
from flask import Response

path = "resources/"
totalSongSize = 5
songs = json.load( open(path + 'songs.json', 'r') )
playlists = json.load( open(path + 'playlists.json', 'r') )
artists = json.load( open(path + 'artists.json', 'r') )



def getPlaylistSongs( body ):
    temp = dict()
    try:
        currentPlaylist = playlists[ str(body['id']) ]
    except:
        return Response( status=210 )
    index = int(body['np'])*totalSongSize                           # npage * limitSize
    temp['lp'] = index+totalSongSize < len( currentPlaylist['g'] )   # last_page
    temp['data'] = list( map( songWrapper, currentPlaylist['g'][ index:totalSongSize+index ] ) )
    return temp

def songWrapper(_id):
    temp = dict()
    temp['id'] = _id
    temp['i'] = songs[_id]['i']
    temp['t'] = songs[_id]['t']
    temp['u'] = songs[_id]['emu']
    return temp

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
        temp['data'].append(  { name: list(map( playlistWrapper, keys )) }  )
    return temp 