#!/usr/bin/env python3

# Network Activity from http://www.zamg.ac.at/histalp/dataset/station/osm.php
JSON = "http://www.zamg.ac.at/histalp/dataset/station/js/statinfo/histalp_stations.json"

import json
import urllib.request


def fetch_json(url):
    req = urllib.request.Request(url)
    f = urllib.request.urlopen(req)
    return json.loads(f.read().decode('ascii'))

def stations(collection):
    for feature in collection['features']:
        print(feature['properties']['k_nam'],
          feature['geometry']['coordinates'])

stations(fetch_json(JSON))
