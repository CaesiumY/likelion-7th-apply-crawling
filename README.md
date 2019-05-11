MJU(Seoul) x Likelion Crawler
-----------------------------

![Version](https://img.shields.io/badge/Version-1.0.0-green.svg) ![Likelion](https://img.shields.io/badge/Likelion-MJU(Seoul)-informational.svg)

### 1. INFO

---

명지대학교(서울) 멋쟁이 사자처럼 7기 서류 수집을 위한 Python 기반 웹 크롤러

### 2. 실행 방법

---

먼저 레파지토리 내의 가상환경(venv)을 실행해준다.

```
source venv/bin/activate
```

이후, pip로 requests, BeautifulSoup, selenium를 각각 설치해준다.

```
pip install requests
pip install bs4
pip install selenium
```

크롬이 로컬 환경에 설치되어 있다는 전제 하에 Chrome WebDriver를 다운로드해준다. 다운로드는 [여기](https://sites.google.com/a/chromium.org/chromedriver/downloads)를 통해 운영체제에 맞게 다운로드한다.

다운로드 후에 Chrome WebDriver 파일의 full path를 복사하여 [parser.py](parser.py) 파일 6번째 줄에 아래처럼 붙여넣기 해준다.

```
driver = webdriver.Chrome("/Users/hanjongwoo/Desktop/개발자도구/Github/likelionmyongji_crawler/chromedriver")
```

이후, [parser.py](parser.py) 파일에서 작은 따옴표안에 각 운영진의 학교에 맞는 XPath를 적어주어야 한다. 멋사 지원 페이지에 운영진 계정으로 로그인 후, 크롬 개발자 모드를 이용하여 "우리 학교 지원자 보기" 버튼의 XPath를 25번째 줄에 넣어주자.

```
driver.find_element_by_xpath('학교별 XPath').click()
```

마지막으로 운영진 계정의 아이디와 비밀번호를 각각 16, 17번째 줄 쌍따옴표 안에 적어준다. 나중에 커밋할 때 계정 정보가 노출되지 않도록 주의하자.

```
username = "운영진 계정 아이디"
password = "운영진 계정 비밀번호"
```

위의 과정을 다 마쳤다면 아래의 명령어를 터미널에 입력하여 서류 크롤러를 작동해보자.

```
python parser.py
```

코드를 실행하면 아래와 같이 총 지원자 수를 묻는데

```
총 지원자 수를 입력해 주세요:
```

지원서를 제출한 인원수를 적으면 된다.
