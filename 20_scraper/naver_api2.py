# coding=utf-8

import requests
import pprint
from requests import Request, Session

headers = {
    'X-Naver-Client-Id': 'Ol8C9WRS2jrclOSdcoud',
    'X-Naver-Client-Secret': 'EzEuo70lri',
}


s = Session()

headers = {
    'X-Naver-Client-Id': 'Ol8C9WRS2jrclOSdcoud',
    'X-Naver-Client-Secret': 'EzEuo70lri',
}

text = "Somewhere over the rainbow way up high"

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/papago/n2mt'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

res_json = res.json()
print(res_json)
print(res_json['message']['result']['translatedText'])


