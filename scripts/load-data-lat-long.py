import os
import django
import requests
import csv
import math
import json
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from xml.etree import ElementTree as ET

# Get the base directory
basepath = Path()
basedir = str(basepath.cwd())
# Load the environment variables
envars = basepath.cwd() / '.env'
load_dotenv(envars)

os.environ["DJANGO_SETTINGS_MODULE"] = 'elderlyhome.settings'
django.setup()

from homes.models import Home

NAVER_GEOCODE_API_URL = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
NAVER_GEOCODE_FIND_HEADERS = {
    'X-NCP-APIGW-API-KEY-ID': os.getenv('NAVER_GEOCODE_CLIENT_ID'),
    'X-NCP-APIGW-API-KEY': os.getenv('NAVER_GEOCODE_CLIENT_SECRET')
}

homes = Home.objects.exclude(address__exact='')
cnt = homes.count()
index = 0
for home in homes:
    if home.is_address_find_done is True and home.is_latlng_find_done is False:
        url = NAVER_GEOCODE_API_URL + '?query=' + home.address
        response = requests.get(url, headers=NAVER_GEOCODE_FIND_HEADERS)
        value = json.loads(response.text)
        try:
            lng = value['addresses'][0]['x']
            lat = value['addresses'][0]['y']
            home.geo_lat = lat
            home.geo_lng = lng
            print(lat, lng)
        except IndexError:
            print('no address')
            pass
        except KeyError:
            print('no key')
            pass
        home.is_latlng_find_done = True
        home.save()
        print(str(index) + '/' + str(cnt) + '  ' + str(round(index/cnt, 3)) + '% DONE')
        # time.sleep(0.12)
        index = index + 1
