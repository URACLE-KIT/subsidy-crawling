# 웹 크롤링 및 데이터 저장 방법(subsidy-crawling)
이 프로젝트는 Python과 BeautifulSoup 패키지를 사용하여 웹 크롤링을 수행하고, 크롤링한 데이터를 MySQL 데이터베이스에 저장하는 방법에 대해 다룹니다.

## crawlingcsv.py
- 웹 크롤링한 데이터를 CSV 파일에 저장하는 방법을 소개합니다.
- 이 방법의 문제점은 크롤링한 데이터를 먼저 CSV 파일에 저장해야 하며, 그 후 CSV 파일을 MySQL Workbench 또는 다른 도구를 사용하여 데이터베이스에 import해야 합니다.
- 이 과정은 데이터 저장 및 import 시간이 소요되므로 전체 실행 시간이 길어질 수 있습니다.

## crawlingdb.py
- 직접 Python을 사용하여 MySQL 데이터베이스에 데이터를 저장하는 방법을 소개합니다.
- 이 방법은 크롤링한 데이터를 중간 저장소(예: CSV 파일)에 저장하지 않고, 바로 MySQL 데이터베이스에 데이터를 입력합니다.
- 이로써 데이터 저장 및 import 시간을 절약하며 전체 실행 속도를 향상시킬 수 있습니다.

각 스크립트 파일은 주석을 포함하여 코드 내용을 자세히 설명하고 있습니다. 프로젝트의 요구 사항과 데이터 처리 방법에 따라 적절한 방법을 선택할 수 있습니다.

## crawlingcategory.py 
- crawlingdb.py와 전체적인 기능은 같지만 category column을 추가하여서 각 category에 맞게끔 페이지가 크롤링되서 MySQL 데이터베이스에 데이터를 입력합니다.
  


## 사용법
1. crawlingcsv.py 또는 crawlingdb.py 스크립트를 실행하기 전에 필요한 패키지를 설치해야 합니다.
2. 스크립트를 실행하여 웹 크롤링 작업을 수행합니다.
3. 데이터를 저장 또는 import하려는 방법에 따라 스크립트를 수정하고 실행합니다.

## 요구 사항
- Python 3.x
- BeautifulSoup 패키지 (웹 크롤링용)
- MySQL 데이터베이스 접속 및 관리 도구 (MySQL Workbench 등)
