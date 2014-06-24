#!/usr/bin/env python3


# Vary the station=_xx number in the request:
"""
curl -d country=IT -d statabbr=BRX -d parameter=T01 -d station=_22 -d years='1896 - 1900' -d exportCSV='foo' http://www.zamg.ac.at/histalp/dataset/station/csv.php
"""
