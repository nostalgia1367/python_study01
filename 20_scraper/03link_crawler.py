import requests
from bs4 import BeautifulSoup

"""
    find(tag, Attributes) # tag.find('div')
    find_all(tag, Attributes)   #tag.find_all('a', href='link3')
    find(class='box')   #CSS 클래스명으로 찾기
    
    정규식으로 찾기
    find(re.compile('^b'))          # b로 시작되는 첫 번째 태그
    find_all(re.compile('t'))       # t를 포함한 모든 태그
    find_all(href=re.compile('[\w][3]')
    
    
    BeautifulSoup
    soup.select("head > title")
    soup.select(".sister")
    soup.select("a#link2")
    soup.select('a[href^="http://example.com/"]')   #특정문자열로 시작
    ㅇ
"""

res = requests.get('http://example.webscraping.com/index/1')
soup = BeautifulSoup(res.text, 'lxml')

for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

