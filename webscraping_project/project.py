import requests
from bs4 import BeautifulSoup
import re


def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36","Accept-Language":"ko-KR,ko"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(idx, title, link):
    print("{}. {}".format(idx+1, title))
    print(" 링크 : {}".format(link))
    print()


def scrape_weather():
    print("오늘의 날씨")
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8'
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()

    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨"," ")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()

    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()

    print(cast)
    print("현재 {} (최저 {} / 최고{})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {} ".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = 'https://news.naver.com'
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li") # , limit=3  3개만 가져오기
    for idx, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(idx, title, link)

    

def scrape_it_news():
    print("[IT 뉴스]")
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li")
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = url + a_tag['href']
        print_news(idx, title, link)


def scrape_english():
    print("[오늘의 영어 한줄]")
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    soup = create_soup(url)
    sentences = soup.find_all('div', attrs={"id":re.compile("^conv_kor_t")})
    print("[영어 지문]")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())

    print()
    print("[한글 지문]")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())


if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 가져오기
    scrape_headline_news()
    scrape_it_news()
    scrape_english()