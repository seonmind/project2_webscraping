from selenium import webdriver
import time


browser=webdriver.Chrome() #"./chromedriver.exe"

browser.get("http://naver.com")
time.sleep(1) #로드 되기전에 element 추출에 들어가면 error 발생함
elem=browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("school1931")
browser.find_element_by_id("pw").send_keys("naverkimsk1931*")
time.sleep(1)
browser.find_element_by_id("log.login").click()

# time.sleep(3)
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("naver2_id")

print(browser.page_source)
# browser.quit()

'''
# element를 여러가지 attribute로 찾기
elem=browser.find_element_by_class_name("link_login")  # elem에 버튼을 받기
elem.click()                                           # 버튼 클릭

# browser를 앞뒤로 이동 새로고침
browser.back()
browser.forward()
browser.refresh()

#키보드 입력값 받기
from selenium.webdriver.common.keys import Keys
elem=browser.find_element_by_id("query")   
elem.send_keys("나도 코딩")
elem.send_keys(Keys.ENTER)

elem=browser.find_elements_by_tag_name("a")
for e in elem:                 
    e.get_attribute("href")

# xpath로 element 찾기
elem=browser.find_element_by_xpath("//*[@id=\"daumSearch\"]/fieldset/div/div/button[2]") 

#종료
browser.close  #현재 탭
browser.quit() #전부 종료
'''