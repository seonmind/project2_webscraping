import requests
import re
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

def create_soup(url, headers):   
    res=requests.get(url,headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    return soup
        
def print_news(index,title,link):
    print("{}. {}".format(index+1,title))
    print(" (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%86%A1%ED%8C%8C%EA%B5%AC+%EC%9E%A0%EC%8B%A4+2%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hgsc2dp0J14ssLhw%2BQossssstvo-162293"
    soup=create_soup(url,headers)
    
    cast=soup.find("p",attrs={"class":"cast_txt"}).get_text().replace(",","/")
    curr_temp=soup.find("p",attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp=soup.find("span",attrs={"class","min"}).get_text()
    max_temp=soup.find("span",attrs={"class","max"}).get_text()
    morning_rain_rate=soup.find("span",attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate=soup.find("span",attrs={"class":"point_time afternoon"}).get_text().strip()
    dust=soup.find("dl",attrs={"class":"indicator"})
    pm10=dust.find_all("dd")[0].get_text()
    pm25=dust.find_all("dd")[1].get_text()


    print(cast)
    print("현제 {} (최저 {} / 최고 {})".format(curr_temp,min_temp,max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate,afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url="https://news.naver.com"
    soup=create_soup(url,headers)
    news_list=soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li",limit=3)
    for idx, news in enumerate(news_list):
        title=news.div.a.get_text().strip()
        link=url+news.find("a")["href"]
        print_news(idx,title,link)
    print()

def scrape_it_news():
    print("[IT 뉴스}")
    url="https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup=create_soup(url,headers)
    news_list=soup.find("div",attrs={"class":"list_body newsflash_body"}).find_all('li',limit=3)
    for idx, news in enumerate(news_list):
        title=news.find_all('a')[1].get_text().strip()
        link=news.find('a')['href']
        print_news(idx,title,link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url="https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup=create_soup(url,headers)
    # kor_lists=soup.find("div",attrs={"class":"conv_txtBox"}).find("div",attrs={"class":"conv_txt"}).find_all('div')
    # eng_lists=soup.find_all("div",attrs={"class":"conv_txtBox"})[1].find("div",attrs={"class":"conv_txt"}).find_all('div')
    # for idx, eng_list in enumerate(eng_lists):
    #     expression=eng_list.get_text().strip()
    #     print(expression)
    # print()
    # for idx, kor_list in enumerate(kor_lists):
    #     expression=kor_list.get_text().strip()
    #     print(expression)
    sentences=soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 표현)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print("(한글 표현)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()
    

if __name__=="__main__":
    scrape_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english()