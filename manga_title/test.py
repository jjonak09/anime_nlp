from bs4 import BeautifulSoup
from time import sleep
import requests

url = "https://comic.k-manga.jp/title/29876/pv"
results = []

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html5lib')
titles = soup.find(class_='book-info--desc')
title = titles.p.text
results.append(title)


with open('test.txt',mode='w') as f:
    for i in range(len(results)):
        f.write(results[i] + '\n')
