# 웹 크롤링 및 데이터 저장 방법(subsidy-crawling)
이 프로젝트는 Python과 BeautifulSoup 패키지를 사용하여 웹 크롤링을 수행하고, 크롤링한 데이터를 MySQL 데이터베이스에 저장하는 방법에 대해 다룹니다.

## crawlingcsv.py
- 웹 크롤링한 데이터를 CSV 파일에 저장하는 방법을 소개합니다.
- 이 방법의 문제점은 크롤링한 데이터를 먼저 CSV 파일에 저장해야 하며, 그 후 CSV 파일을 MySQL Workbench 또는 다른 도구를 사용하여 데이터베이스에 import해야 합니다.
- 이 과정은 데이터 저장 및 import 시간이 소요되므로 전체 실행 시간이 길어질 수 있습니다.

## crawlingexist.py 
- 직접 python을 사용하여 MySQL 데이터베이스에 데이터를 저장하는 방법입니다. 
- 이 방법은 크롤링한 데이터를 중간 저장소 (ex: csv파일)에 저장하지 않고, 바로 MySQL 데이터베이스에 데이터를 입력합니다. 
- 이로써 데이터 저장 및 import 시간을 절약하며 전체 실행 속도를 향상 시킬 수 있습니다. 
- 크롤링 진행 중 해당 데이터가 DB 안에 존재하면 스킵을 하고 , 새로운 데이터면 DB에 저장을 합니다.
- 정부 24로부터 크롤링한 데이터는 매주 월요일 00:00 시에 업데이트가 자동으로 진행됩니다.  

## 사용법
1. crawlingcsv.py 또는 crawlingexist.py 스크립트를 실행하기 전에 필요한 패키지를 설치해야 합니다.
```bash
pip install requests
```
```bash
pip install beautifulsoup4
```
```bash
pip pip install pymysql
```
```bash
pip pip install schedule
```
2. 스크립트를 실행하여 웹 크롤링 작업을 수행합니다.

```bash
python ./crawlingcsv.py
```

```bash
python ./crawlingexist.py
```

3. 데이터를 저장 또는 import하려는 방법에 따라 스크립트를 수정하고 실행합니다.


## 요구 사항
- Python 3.x
- BeautifulSoup 패키지 (웹 크롤링용)
- MySQL 데이터베이스 접속 및 관리 도구 (MySQL Workbench 등)
