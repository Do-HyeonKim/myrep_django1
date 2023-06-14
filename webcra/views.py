from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import time

@api_view(['POST'])
def test(request) : 

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    path  = 'C:\\chromedriver\\chromedriver.exe'
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=  service , options=options)

    url = "https://play.google.com/store/movies/stream/promotion_collections_movie_studios?hl=ko&gl=US"

    driver.get(url)
    driver.maximize_window()

    time.sleep(3)

    body = driver.find_element(By.CSS_SELECTOR, 'div.N4FjMb.Z97G4e')
    move_titles = body.find_elements(By.CSS_SELECTOR, 'div.Epkrse')
    # 이전에 가져온 요소들을 저장할 변수

    # 스크롤 내리기
    actions = ActionChains(driver)
    actions.move_to_element(body)
    actions.send_keys(Keys.END)
    time.sleep(10)
    actions.send_keys(Keys.END)
    actions.perform()

    # 잠시 대기
    time.sleep(20)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='Epkrse')

    title_list=  []
    for title in titles : 
        title_list.append(title.get_text())

    print(title_list)


    return Response()

@api_view(['POST'])
def test3(request) : 

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    path  = 'C:\\chromedriver\\chromedriver.exe'
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=  service , options=options)

    url = "https://www.29cm.co.kr/shop/category/list?category_large_code=273100100&category_medium_code=&sort=new"

    driver.get(url)
    driver.maximize_window()

    time.sleep(3)

    # body = driver.find_element(By.CSS_SELECTOR, 'div.N4FjMb.Z97G4e')
    # move_titles = body.find_elements(By.CSS_SELECTOR, 'div.Epkrse')
    # 이전에 가져온 요소들을 저장할 변수

    # 스크롤 내리기
    actions = ActionChains(driver)
    # actions.move_to_element(body)
    actions.send_keys(Keys.END)
    time.sleep(5)
    actions.perform()

    # 잠시 대기
    # time.sleep(20)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='name')

    title_list=  []
    for title in titles : 
        title_list.append(title.get_text())

    print(title_list)


    # list insert 코드 여기 부분 추가 
    # orm인 경우 .exsist()로 확인 orm | 아닌 경우 count =1 있는지 확인 후 없는경우에만 insert 로직 실행
    # list별로 url 돌아야함 
    # device.get(리스트별url)
    # 두번째 영역 클릭 후 keys.END 실행 후 다시 bs4로 html 요소 저장 i부터 시작 [ 0 부터 3의 배수만 ]
    #     new_list = []
    #     for i, signal in enumerate(signal_list):
    #     if i % 3 == 0:
    #         new_list.append(signal.text)
    # 요소 전체 저장 후 insert 문 실행 for 문 끝나기 전에 new_list for문 돌면서 insert문 실행해야함
    # 마찬가지로 orm 인 경우 .exisit() 확인 아닌 경우 | count = 1
    # 두번째 영역 저장 시에는 where 조건문에 id / param 둘 다 비교해야함 [ 저장 시 저장 날짜 year-month ] 


    return Response()


@api_view(['POST'])
def test2(request) : 

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    path  = 'C:\\chromedriver\\chromedriver.exe'
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=  service , options=options)

    url = "https://play.google.com/store/movies/stream/promotion_collections_movie_studios?hl=ko&gl=US"

    driver.get(url)

    time.sleep(3)

    body = driver.find_element(By.CSS_SELECTOR, 'div.N4FjMb.Z97G4e')
    # move_titles = body.find_elements(By.CSS_SELECTOR, 'div.Epkrse')
    # 데이터를 저장할 리스트 초기화
    b_list = []

# 스크롤을 내리며 데이터 수집
    while True:
        # 현재 스크롤 위치에서 b 요소의 텍스트 수집
        elements = body.find_elements(By.CSS_SELECTOR, 'div.Epkrse')
        move_title = [element.text for element in elements]
        b_list.extend(move_title)

        # 스크롤을 다음 위치로 이동
        actions = ActionChains(driver)
        actions.move_to_element(body)
        actions.send_keys(Keys.END)
        actions.perform()
        time.sleep(2) # 스크롤 동작을 위한 잠시 대기

        # 새로운 b 요소가 나타날 때까지 대기
        WebDriverWait(body, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.Epkrse')))

        # 새로운 b 요소가 더 이상 나타나지 않으면 반복 종료
        if len(body.find_elements(By.CSS_SELECTOR, 'div.Epkrse')) == len(elements):
            break

    # 데이터 출력
    print(b_list)

    return Response()