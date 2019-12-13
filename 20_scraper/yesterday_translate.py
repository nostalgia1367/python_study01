# coding=utf-8

from requests import Request
from requests import Session
import os
import sys

s = Session()

fileName = 'yesterday.txt'

# function : 텍스트 번역 함수
def translate(str_yesterday):
    headers = {
        'X-Naver-Client-Id': 'Ol8C9WRS2jrclOSdcoud',
        'X-Naver-Client-Secret': 'EzEuo70lri',
    }

    payload = {
        'source': 'en',
        'target': 'ko',
        'text': str_yesterday,
    }

    url = 'https://openapi.naver.com/v1/papago/n2mt'

    req = Request('POST', url, data=payload, headers=headers)
    prepped = req.prepare()

    res = s.send(prepped)

    print(res)
    return res.json()['message']['result']['translatedText']

# function : 파일 열어서 변수에 담는 함수
def file_open(fileName):
    str_yesterday = ''
    try:
        with open(fileName, mode='rt') as f:

            while True:
                line = f.readline()
                if not line: break
                str_yesterday += line.splitlines()[0] + '\n'

            # print(str_yesterday)

    except:
        sys.stderr.write("Not find File: %s\n" % fileName)
        exit(1)

    else:
        return str_yesterday


# function : 번역한 텍스트를 파일로 생성하는 함수
def file_translate(text):

    f = open('yesterday_translate.txt', mode='wt')
    f.write(text)
    f.close()


def main():
    str_yesterday = file_open('yesterday.txt')
    print(str_yesterday)

    print('번역을 시작합니다.')
    str_translate = translate(str_yesterday)
    print(str_translate)
    print('번역을 완료되었습니다.')

    # 파일로 저장
    file_translate(str(str_yesterday) + str(str_translate))


if __name__=='__main__':
    main()




