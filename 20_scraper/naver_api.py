# coding=utf-8

import requests
import pprint

headers = {
    'X-Naver-Client-Id': 'Ol8C9WRS2jrclOSdcoud',
    'X-Naver-Client-Secret': 'EzEuo70lri',
}

payload = {
    'query': '카카오',
    'display' : 100
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)

print('요청성공..')
print(res)

result = res.json()['items'][2]['title']

# pprint.pprint(res.json())
print(result)

