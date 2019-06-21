#!/usr/bin/python

# import SocketServer, SimpleHTTPServer
import requests
import sqlite3
import  sys
try:
    import simplejson as json
except ImportError:
    import json


def get_data(url):
    print("in get_data()")
    r = requests.get(url)
    print("requests.get() complete")
    if r.status_code != 200:
        return ["bad json"]
    return r.json()

def main():
    year = input("input year:   ")
    print("starting...")
    global all
    # Read data before starting the server.
    data = 'https://www.surfrider.org/bwtf/labs/samples/4'
    print("data being read...")
    all = get_data(data)
    print("data read.")

    numSamples = len(all['samples'])
    print(numSamples)
    
    samples = all['samples']
    totalCount = 0
    totalBac = 0
    yearCount = 0
    yearBac = 0
    bac = 0
    for i in range(0,numSamples):
        if samples[i]['enterobacteria'] is not None:
            bac = samples[i]['enterobacteria']
        if (year == samples[i]['date'][:4]):
            # name = str(samples[i]['siteName'])
            
            # print("(site):%50s (entero):%10s " % (name , bac))
            yearCount += 1
            yearBac += int(bac)

        totalCount += 1
        totalBac += int(bac)
    
    print("total enterobacteria in all samples:      " + str(totalBac))
    print("samples taken in the year " + str(year) + ":   " + str(yearCount))
    print("total enterobacteria in given year:       " + str(yearBac))
    print("average entero per sample in all samples: " + str(totalBac/totalCount))
    print("average entero per sample in given year:  " + str(yearBac/yearCount))

main()