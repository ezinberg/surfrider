import SocketServer, SimpleHTTPServer, requests
import sqlite3
import web, sys
try:
    import simplejson as json
except ImportError:
    import json


def get_data(url):
    r = requests.get(url)
    if r.status_code != 200:
        return ["bad json"]
    return r.json()

def main():
    print("starting...")
    global all
    # Read data before starting the server.
    data = 'https://www.surfrider.org/bwtf/labs/samples/4'
    all = get_data(data)

    numSamples = len(all['samples'])
    print numSamples