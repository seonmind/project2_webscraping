import csv
import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename="시가총액1-200.csv"

# utf-8-sig로 인코딩시 csv파일을 엑셀로 열떄 깨짐현상 해결
f=open(filename,"w",encoding="utf8",newline="") #newline을 안해주면 자동으로 한줄씩 공백 줄바꿈이 들어감
writer=csv.writer(f)
# split은 인자를 기준으로 문자열을 잘라서 리스트 형태로 저장
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)
for page in range(1,5):
    res=requests.get(url+str(page))
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'lxml')

    data_rows=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns=row.find_all("td")
        # 빈칸 생성용 td를 제거
        if len(columns)<=1:
            continue

        # strip함수: 인자 안에 들어간 캐릭터를 문자열 앞/뒤에서 제거해나가다 
        # 제거대상이 아닌 캐릭터가 나오면 문자열 가공 중지
        data=[column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)#리스트를 안에 집어넣어서 써줌