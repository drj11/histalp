#!/usr/bin/env python3

import json
import re
import urllib.request

# URL from the SCRIPT tag at this URL:
#   view-source:http://www.zamg.ac.at/histalp/dataset/station/csv.php
URL = "http://www.zamg.ac.at/histalp/dataset/station/js/statinfo/20140520102545_histalp_statinfo.js"

def get_json(url):
    req = urllib.request.Request(url)
    f = urllib.request.urlopen(req)
    nearly_json = f.read().decode('ascii')
    j = nearly_json.split('\n')[1]
    j = re.sub(r'^.*?=', '', j)
    json_string = re.sub(r';\s*$', '', j)
    return json.loads(json_string)

def get_all_stations(countries):
    """
    Takes a dictionary keyed by country code, returns a
    dictionary keyed by station number (which all start with
    "_").
    """
    result = dict()
    for country_code, d in countries.items():
        result.update(d['stations'])
    return result

def filter_temperature_stations(stations):
    """
    Returns a fresh dictionary that includes only stations
    that are reporting a T01, average monthly temperature,
    parameter.
    """

    result = dict()
    for histalp_id,station in stations.items():
        if 'T01' in station['params']:
            result[histalp_id] = station
    return result

def main():
    country_stations = get_json(URL)
    all_stations = get_all_stations(country_stations)
    temperature_stations = filter_temperature_stations(all_stations)
    for histalp_id, station in temperature_stations.items():
        t_param = station['params']['T01']
        print(station['abbr'], station['name'],
          t_param['min'], t_param['max'])


if __name__ == '__main__':
    main()

