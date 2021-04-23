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

NAVER_ADDRESS_API_URL = 'https://openapi.naver.com/v1/search/local.json'
NAVER_ADDRESS_FIND_HEADERS = {
    'X-Naver-Client-Id': os.getenv('NAVER_ADDRESS_CLIENT_ID'),
    'X-Naver-Client-Secret': os.getenv('NAVER_ADDRESS_CLIENT_SECRET')
}

homes = Home.objects.all()

for home in homes:
    if not home.is_address_find_done:
        url = NAVER_ADDRESS_API_URL + '?query=' + home.sigungu_code.sigungu_name + ' ' + home.home_name
        response = requests.get(url, headers=NAVER_ADDRESS_FIND_HEADERS)
        value = json.loads(response.text)
        print(value)
        try:
            address = value['items'][0]['address']
            print(address)
            # home.address = address
        except IndexError:
            print('no address')
            pass
        except KeyError:
            print('no key')
            pass
        # home.is_address_find_done = True
        # home.save()
        time.sleep(0.12)
