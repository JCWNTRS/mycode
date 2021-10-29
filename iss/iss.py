#!/usr/bin/env python3

import requests as rq

URL = "http://api.open-notify.org/iss-now.json"

iss_loc = rq.get(URL).json()
print("CURRENT LOCATION OF THE ISS: ")
print("longitude: ", iss_loc['iss_position']['longitude'])
print("latitude: ", iss_loc['iss_position']['latitude'])
print("Timestamp: ", iss_loc['timestamp'])
