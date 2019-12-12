# coding=utf-8

from requests import Request
from requests import Session
import os


s = Session()

headers = {
    'X-Naver-Client-Id': 'Ol8C9WRS2jrclOSdcoud',
    'X-Naver-Client-Secret': 'EzEuo70lri',
}

text = "Yesterday all my troubles seemed so far away."

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/papago/n2mt'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

# print(res.json())
# print(res.json()['message'])

result = res.json()['message']['result']['translatedText']

print(result)

def file_open():
    fileTxt = os.open('yesterday.txt', 'r')

    print(fileTxt)



def main():
    print('메인시작')
    file_open()


if __name__=='__main__':
    main()