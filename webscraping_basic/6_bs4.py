import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)

res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml") #lxml을 통해서 html을 분석하여 soup객체로 만듦

# print(soup.title)                 # soup을 통해 html 밑의 특정 엘리먼트의 정보를 불러올 수 있음
# print(soup.title.get_text())      #그중 텍스트만
# print(soup.a)                     #soup 객체에서 처음 발견되는 a만
# print(soup.a.attrs)               #엘리먼트의 속성 정보 출력
# print(soup.a["href"])             #엘리먼트의 특정 속성 '값' 정보 출력


soup.find("a", attrs={"class":"Nbtn_upload"}) #처음 발견되는 a 엘리먼트에서 해당 조건을 만족하는 것을 찾음  
rank1= soup.find("li",attrs={"class":"rank01"}) 

# tag사이에서 부모나 자식 형제간의 이동이 가능

# print(rank1)
# print(rank1.a)                           #자식관계
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling)   #다음 형제관계의 태그에 접근 중(두번한 이유는 여기선 한번하면 줄바꿈)
# print(rank1.parent)
# rank2=rank1.find_next_sibling("li")      #해당 조건을 만족하는 형제관계 태그가 찾아짐
# rank3=rank2.find_previous_sibling("li")  #이전 형제관계의 태그에 접근
# print(rank1.next_siblings)               #다 가져오기

# we=soup.find("a",text="")   특정 텍스트를 가진 태그를 불러옴