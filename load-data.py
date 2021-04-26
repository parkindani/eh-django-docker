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
from decimal import Decimal

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
    if home.is_address_find_done is True and home.is_latlng_find_done is True and home.geo_lat != '':
        str_geo_lat = home.geo_lat
        str_geo_lng = home.geo_lng
        dec_geo_lat = Decimal(str_geo_lat)
        dec_geo_lng = Decimal(str_geo_lng)
        home.geo_lat_decimal = dec_geo_lat
        home.geo_lng_decimal = dec_geo_lng
        home.save()
        print(str(index) + '/' + str(cnt) + ' | ' + str(round(index/cnt*100)) + '% DONE :: ' + home.home_name)
        index = index + 1
