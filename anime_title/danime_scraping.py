from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome(executable_path="chromedriverのパス")
driver.get("アクセスするURL")
results = []

html01 = driver.page_source
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    html02 = driver.page_source
    if html01 != html02:
        html01 = html02
    else:
        break
soup  = BeautifulSoup(html01,"html.parser")
titles = soup.find_all(class_ = 'textContainerIn')

for title in titles:
    anime_title = title.find(class_='ui-clamp webkit2LineClamp').get_text()
    results.append(anime_title)

driver.close()
driver.quit()


with open('suspense.txt',mode='w') as f:
    for i in range(len(results)-1):
        f.write(results[i] + '\n')
