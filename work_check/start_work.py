# 필요한 라이브러리
import os
from selenium import webdriver

# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
# 절대경로를 상대경로로 바꿔주는 함수
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 실행 파일의 상위 경로에 있는 폴더에서 ID와 PASSWORD를 불러옴
with open(resource_path('../personal/ID.txt'), 'r') as f:
    ID = f.read()

with open(resource_path('../personal/PWD.txt'), 'r') as b:
    PWD = b.read()

# 크롬 드라이버를 설정
options = webdriver.ChromeOptions()

# 필요없는 에러로그가 뜨지 않게함(프로그램상 문제가 없음)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 불러오기
driver = webdriver.Chrome(resource_path('../chromedriver.exe'), options=options)

# 출퇴근 사이트 주소로 접속
driver.get('https://................')

# 로딩을 위해 3초 기둘
driver.implicitly_wait(3)

# ID, PASSWORD의 위치를 찾아 입력한 뒤, 로그인 버튼을 클릭
driver.find_element_by_xpath('//*[@id="emp_no"]').send_keys(ID)
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(PWD)
driver.find_element_by_xpath('//*[@id="login"]/fieldset/div[1]/ul[3]/li[1]/a').click()

# 로딩을 위해 3초 기달
driver.implicitly_wait(3)

# 여러 개의 프레임 중 '출근하기' 버튼이 있는 프레임으로 이동
driver.switch_to.frame(driver.find_element_by_name('bodyframe'))

# '출근하기' 클릭
driver.find_element_by_xpath('/html/body/form/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/ul/li[1]/a').click()

# 출근했다는 알림창 확인
Alert(driver).accept()

# 부끄러우므로 드라이버를 끄도록 한다.
driver.close()

# pyinstaller로 exe 파일 변환, 작업 스케줄러로 윈도우가 켜질 때 실행되도록 하였다.
