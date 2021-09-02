import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

url="https://www.daum.net/"
browser=webdriver.Chrome()
browser.get(url)
browser.maximize_window()

browser.find_element_by_id("q").send_keys("송파 헬리오시티")
browser.find_element_by_id("q").send_keys(Keys.ENTER)

time.sleep(2)
soup=BeautifulSoup(browser.page_source,"lxml")

# with open("check.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
items=soup.find_all('div',attrs={"class":"cont_info"})
print(len(items))