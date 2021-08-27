import requests
# 웹에서 url을 통해 html을 불러옴
res=requests.get("http://google.com")
print("응답코드: ",res.status_code) #그 서버의 응압상태? 200은 정상 403 접근 권한 무

# 응답코드에 따라 정상이 아니면 에러를 띄우도록 if문
# if res.status_code==requests.codes.ok
# 그대신 특정함수 사용 정상이 아니면 에러가 나옴
res.raise_for_status

# 구글 html을 불러와 파일로 만들기

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)