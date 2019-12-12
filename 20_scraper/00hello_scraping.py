import requests
from requests.exceptions import ConnectionError

"""
    res.headers
    res.encoding
    res.text
    res.json()

"""

def download(url):
    print('Downloading:', url)
    try:
        html = requests.get(url)
    except ConnectionError as err:
        print(err)
        html = None
    return html


def main():
    html = download('http://example.webscraping.com')
    print(html)


if __name__ == '__main__':
    main()
