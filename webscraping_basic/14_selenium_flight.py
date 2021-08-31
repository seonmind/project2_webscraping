from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser=webdriver.Chrome()
browser.maximize_window()

url="https://beta-flight.naver.com/"
browser.get(url)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
# 로딩될 때까지 기다리는 거
# try:
elem=WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/button")))
# finally:
#         browser.quit()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/button").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/button").click()

