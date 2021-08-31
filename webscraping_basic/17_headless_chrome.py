from selenium import webdriver

# 브라우저 실제로는 안켜고 background에서만 돌리기
options=webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080")
# headless 크롬 사용시 접속이 막아지는거 예방용 user agent 설정
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")

browser=webdriver.Chrome(options=options)
browser.maximize_window()
url="https://play.google.com/store/movies/top"
browser.get(url)



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

browser.get_screenshot_as_file("google_movie.png") #스크린샷 따기


import requests
from bs4 import BeautifulSoup

soup=BeautifulSoup(browser.page_source,'lxml')

movies=soup.find_all('div',attrs={"class":"vU6FJ p63iDd"})

print(len(movies))

for movie in movies:
    title=movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

