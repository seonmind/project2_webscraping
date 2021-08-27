# 접속자가 컴퓨터인지 휴대폰인지 어떤 브라우저인지에 대한 인자
# user agent string 을 통해 본인거 검색가능


import requests

url="http://nadocoding.tistory.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

res=requests.get(url,headers=headers)

res.raise_for_status
with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)