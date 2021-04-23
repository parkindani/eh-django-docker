import os
import django
import requests
import csv

from xml.etree import ElementTree

os.environ["DJANGO_SETTINGS_MODULE"] = 'elderlyhome.settings'
django.setup()

from homes.models import Sigungu, Sido

WHOLE_SEARCH_URL = 'http://apis.data.go.kr/B550928/searchLtcInsttService/getLtcInsttSeachList'
WHOLE_SEARCH_API_KEY = '7VNKCOoEs9UMYSx%2B7ksl2Tccbio3kT4xLLVFQhqnCf7DEZdaJEYnRIg2kKECa1OkN7DIFqNCI5mGetBCED7CwQ%3D%3D'
#
# sigungus = Sigungu.objects.all()
#
# for sigungu in sigungus:
#     url = WHOLE_SEARCH_URL + '?serviceKey=' + WHOLE_SEARCH_API_KEY + '&siDoCd=' + sigungu.sido_code + '&siGunGuCd=' + sigungu.sigungu_code
#     response = requests.get(url)
#     print(response.text)


# url = WHOLE_SEARCH_URL + '?serviceKey=' + WHOLE_SEARCH_API_KEY
# response = requests.get(url)
#
# print(response.request.url)
# print(response.request.body)
# print(response.request.headers)
# print(response.text)
# tree = ElementTree.fromstring(response.content)
#
# print(tree[0][0])

sidos = Sido.objects.all()

for sido in sidos:
    sigungus = Sigungu.objects.filter(sido_code=sido.id)
    for sigungu in sigungus:
        url = WHOLE_SEARCH_URL + '?serviceKey=' + WHOLE_SEARCH_API_KEY + '&siDoCd=' + sido.sido_code + '&siGunGuCd=' + sigungu.sigungu_code
        response = requests.get(url)
        print(response.text)


# f = open('./homes/data/sigungu_code.csv', 'r', encoding='utf-8-sig')
#
# rdr = csv.reader(f)
# for row in rdr:
#     print(row)
#     sido = Sido.objects.get(sido_code=row[0])
#     s = Sigungu.objects.create(sigungu_name=row[2], sigungu_code=row[1], sido_code=sido)

# f = open('./homes/data/sido_code.csv', 'r', encoding='utf-8-sig')
#
# rdr = csv.reader(f)
# for row in rdr:
#     print(row)
#     s = Sido.objects.create(sido_name=row[1], sido_code=row[0])
