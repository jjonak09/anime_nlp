from bs4 import BeautifulSoup
from time import sleep
import requests

url = "https://comic.k-manga.jp/search/category/2?search_option%5Bsort%5D=popular&page="
results = []
for i in range(1,98):
    sleep(2)
    r = requests.get(url+str(i))

    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.find_all(class_='book-list--target')

    for title in titles:
        mange_title = title.find(class_='book-list--title').get_text()
        mange_tag = title.find(class_='icon-text icon-text__genre').get_text()
        mange_img_url = title.find('img',class_='book-list--img').get('src')

        mange_url = title.find(class_='book-list--item').get('href')
        sleep(3)
        r2 = requests.get('https://comic.k-manga.jp'+mange_url)
        soup2 = BeautifulSoup(r2.text,'html.parser')
        summary = soup2.find(class_='book-info--desc')
        mange_summary = summary.p.text

        mange = mange_title +',https://comic.k-manga.jp'+ mange_url +','+mange_summary+','+mange_tag+','+mange_img_url
        print(mange)
        results.append(mange)



with open('mange_title.txt',mode='w') as f:
    for i in range(len(results)):
        f.write(results[i] + '\n')
