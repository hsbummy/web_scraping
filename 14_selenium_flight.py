from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27일, 28일 선택

# browser.find_elements_by_link_text("27")[0].click() # [0] > 이번달선택
# browser.find_elements_by_link_text("28")[0].click() # [0] > 이번달선택

# browser.find_elements_by_link_text("27")[1].click() # [0] > 다음달선택
# browser.find_elements_by_link_text("28")[1].click() # [0] > 다음달선택

browser.find_elements_by_link_text("27")[0].click() # [0] > 이번달선택
browser.find_elements_by_link_text("28")[1].click() # [0] > 다음달선택

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    # 성공했을 때 동작 수행
    print(elem.text) # 첫 번째 결과 출력
finally:
    browser.quit()
# 첫 번째 결과 출력

# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)