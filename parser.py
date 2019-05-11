import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# webdriver 주소
path = '\\Users\\mn065\\Desktop\\LionProject1\\likelionmyongji_crawler\\chromedriver.exe'

# chromedriver(macOS 기준) 위치 지정
driver = webdriver.Chrome(path)

# 총 지원자 수 입력(지원서 제출한 인원)
print("총 지원자 수를 입력해 주세요:")
recruitNum = int(input())

# 웹 자원 로드를 위해 암묵적으로 딜레이
delay_time = 3
driver.implicitly_wait(delay_time)

# URL 접근
driver.get('https://apply.likelion.org/accounts/login/?next=/apply/')

# 지원 페이지 학교 관리자 ID, PW 입력
username = ""
password = ""
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

# 로그인 버튼 클릭
driver.find_element_by_xpath(
    '//html/body/main/div[2]/div/div/div/form/div[3]/button').click()

# 지원자 보기 버튼 클릭(명지대학교(서울) 멋사 지원자 XPath, 구글 개발자모드에서 복사 후 붙여넣기)
driver.find_element_by_xpath('//*[@id="likelion_num"]/div[2]/a/button').click()

# 저장할 파일 불러오기(recruit.txt)
file = open('recruit.txt', 'w', encoding='utf-8')

# 접수 버튼 XPath 클릭 반복(range(1, 총 지원자수+1))
for recruitXpath in range(1, recruitNum+1):
    # 접수 버튼 XPath 생성
    recruitXpath = '//*[@id="likelion_num"]/div[3]/a[' + \
        str(recruitXpath) + ']/div/div[2]/button'

    # 지원서 서류 접수 버튼 클릭
    driver.find_element_by_xpath(recruitXpath).click()

    # 지원서 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # h3 : 지원자 성함 , p : 지원서 내용
    recruitList = soup.select('h3, p')

    # 지원서 내용 순차 출력
    for n in recruitList:
        # 터미널 출력
        print(n.text.strip())
        print("\n")
        # 파일에 출력
        file.write(n.text.strip())
        file.write("\n\n")

    # 지원서 구분
    print("-----"*5)
    print("\n")
    file.write("-----"*5)
    file.write("\n")
    # 뒤로 가기
    driver.back()

# 작업 마침
print("작업을 마쳤습니다.")
file.close()
driver.close()
