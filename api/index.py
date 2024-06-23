from flask import Flask, request, Response, redirect
import requests as SendRequesttoWeb
# from fake_useragent import UserAgent
# ua = UserAgent()
try:
    from music import *
except:
    from api.music import *



app = Flask(__name__)
session = SendRequesttoWeb.session()
# jioSaavan_req_headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0" }

@app.route( "/getSongName", methods = [ 'POST' ] )
def get_song_name():
    try:
        return getSongTitle(request.json)
    except KeyError as e:
        print(e)
        return Response( '', status=401 )

@app.route( "/getSong", methods = ['POST'] )
def get_song():
    return getSongPath( request.json )

@app.route( "/playlistSongs", methods = [ 'POST' ] )
def get_PlaylistSongs():
    try:
        return getPlaylistSongs( request.json )
    except KeyError as e:
        print(e)
        return Response( '', status=401 )
    
@app.route( "/getMusicImage", methods=['POST']  )
def getMusicImage():
    res = request.json
    return getImage( res['t'], res['id'], res['s'] )

@app.route( "/homepage", methods = ['POST', 'GET'] )
def get_samplePlaylists():
    temp = getArranger()
    temp['n']=12356789
    return temp

@app.route( "/Todaynews", methods = [ 'POST' ] )
def getTodayNews():
    return { 'wn':[ 'war', 'rebel', 'threat' ], 'lp':[ 'election', 'school', 'work' ], 'ln':['accident', 'block', 'bad weather'],  'wp':[ 'new vaccine', 'growth', 'new discovery' ] }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__ == "__main__":
	app.run(debug=True)