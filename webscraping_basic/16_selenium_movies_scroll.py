from selenium import webdriver
browser=webdriver.Chrome()
browser.maximize_window()
url="https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터의 해상도 높이인 1080 위치로 스크롤 내리기 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")
# # 로딩된 것중에서 끝까지 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval=2
prev_height=browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)
    curr_height=browser.execute_script("return document.body.scrollHeight")
    if curr_height==prev_height:
        break
    prev_height=curr_height

import requests
from bs4 import BeautifulSoup

soup=BeautifulSoup(browser.page_source,'lxml')

movies=soup.find_all('div',attrs={"class":"vU6FJ p63iDd"})

print(len(movies))

for movie in movies:
    title=movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

