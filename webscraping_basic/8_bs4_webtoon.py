import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=736989&weekday=thu"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

# cartoons=soup.find_all("td",attrs={"class":"title"})

# 만화 제목 링크 가져오기 샘플
# title=cartoons[0].a.get_text()
# link=cartoons[0].a["href"] #태그의 속성을 대괄호로 접근 가능
# print(title)
# print("https://comic.naver.com"+link)

# 만화 제목과 링크 가져오기
# for cartoon in cartoons:
#     title=cartoon.a.get_text()
#     link="https://comic.naver.com"+cartoon.a["href"]
#     print(title,link)

# 평점 평균 구하기
cartoons=soup.find_all("div",attrs={"class":"rating_type"})
sum=0
for cartoon in cartoons:
    rate=float(cartoon.strong.get_text())
    sum+=rate
print(sum)
print(sum/len(cartoons))

