import os
import django
import requests
import csv
import math
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
# Get the base directory
basepath = Path()
basedir = str(basepath.cwd())
# Load the environment variables
envars = basepath.cwd() / '.env'
load_dotenv(envars)

from xml.etree import ElementTree as ET

os.environ["DJANGO_SETTINGS_MODULE"] = 'elderlyhome.settings'
django.setup()

from homes.models import Sigungu, Sido, Home

WHOLE_SEARCH_URL = 'http://apis.data.go.kr/B550928/searchLtcInsttService/getLtcInsttSeachList'
WHOLE_SEARCH_API_KEY = os.getenv('WHOLE_SEARCH_API_KEY')

sigungus = Sigungu.objects.all()

index = 0

for sigungu in sigungus:
    sido = Sido.objects.get(sido_code=sigungu.sido_code.sido_code)

    url = WHOLE_SEARCH_URL + '?serviceKey=' + WHOLE_SEARCH_API_KEY + '&siDoCd=' + str(sigungu.sido_code.sido_code) + '&siGunGuCd=' + sigungu.sigungu_code
    # print(url)
    response = requests.get(url)
    root = ET.fromstring(response.text)
    totalCount = int(root.find('body').find('totalCount').text)
    ceilCount = math.ceil(totalCount / 10)
    for i in range(ceilCount):
        pageUrl = url + '&pageNo=' + str(i + 1) + '&numOfRows=10'
        pageResponse = requests.get(pageUrl)
        pageRoot = ET.fromstring(pageResponse.text)
        item_array = pageRoot.find('body').find('items')
        items = item_array.findall('item')
        for item in items:
            adminNm = item.find('adminNm').text
            adminPttnCd = item.find('adminPttnCd').text
            longTermAdminSym = item.find('longTermAdminSym').text

            if Home.objects.filter(lt_sym_code=longTermAdminSym).count() == 0:
                h = Home.objects.create(
                    home_name=adminNm,
                    sido_code=sido,
                    sigungu_code=sigungu,
                    pttn_code=adminPttnCd,
                    lt_sym_code=longTermAdminSym,
                    address='',
                    geo_lat='',
                    geo_lng='',
                    max_capacity=0,
                    current_person=0,
                    created_date=datetime.now(),
                    updated_date=datetime.now()
                )
                print(index, sigungu.sigungu_name, adminNm)
                index = index + 1
            else:
                print(index, 'pass')
                index = index + 1
