import requests
from bs4 import BeautifulSoup
import csv

# CSV 파일에 저장할 데이터 리스트
data_list = []

# 반복 횟수 
start_page = 1
end_page = 836

# startCount 
page_count = 0

# startCount 
page_count = 0 

# id 
id = 1
for page in range(start_page, end_page+1):
    for card_count in range(1,13):
        # page 마지막 데이터 id
        if(id == 10024):
            break
        url = f'https://www.gov.kr/portal/rcvfvrSvc/svcFind/svcSearchAll?cityDoArea=ALL&siGunGuArea=ALL&sidocode=ALL&svccd=ALL&tccd=ALL&meancd=ALL&chktype1=&startCount={page_count}&sortOrder=DESC&collection=&range=&startDate=&endDate=&searchField=&reQuery=2&stQuery=&downOrgCd=&cityDoArea=ALL&siGunGuArea=ALL&tmpReQuery=&tmpExReQuery=&reSerachQuery=&realQuery=&detailLst=0&sort=RANK&query=&orgSel=ALL&showView=view22#none'

        # 웹 페이지 내용 가져오기
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        card_box = soup.find('div', class_=f'card-item svc_{card_count}')
        
        # 지원금 상세정보 URL
        detail_information_url_tag = card_box.find('div', class_='card-head').find('a')
        detail_information_url = detail_information_url_tag['href'] if detail_information_url_tag else ''

        # 지원금 제목
        subsidy_title_tag = card_box.find('div', class_='card-head').find('a')
        subsidy_title = subsidy_title_tag.text if subsidy_title_tag else ''

        # 지원금 내용
        subsidy_desc_tag = card_box.find('p', class_='card-desc')
        subsidy_desc = subsidy_desc_tag.text if subsidy_desc_tag else ''

        ul = card_box.find('ul')

        # 신청기간
        frist_li = ul.find_all('li')[0] if ul else None
        subsidy_application_period = frist_li.find('span', class_='card-text').text if frist_li else ''

        # 접수기관
        second_li = ul.find_all('li')[1] if ul else None
        subsidy_receiving_agency = second_li.find('span', class_='card-text').text if second_li else ''

        # 전화문의
        third_li = ul.find_all('li')[2] if ul else None
        subsidy_telephone_inquiry = third_li.find('span', class_='card-text').text if third_li else ''

        # 지원형태
        forth_li = ul.find_all('li')[3] if ul else None
        subsidy_support_type = forth_li.find('span', class_='card-text').text if forth_li else ''

        # 신청방법
        fifth_li = ul.find_all('li')[4] if ul else None
        span_tag = fifth_li.find('span') if fifth_li else None
        subsidy_application_process = span_tag.text if span_tag else ''

        # 신청방법 URL
        fifth_li_atag = fifth_li.find('a') if fifth_li else None
        subsidy_application_process_url = fifth_li_atag.get('href') if fifth_li_atag else ''


        # url이 js로 걸려있을 경우 
        if(subsidy_application_process_url == 'javascript://'):
            subsidy_application_process_url = ''
        
        data_list.append({'id': id, 'title' : subsidy_title, 'detail_information_url': 'https://www.gov.kr'+ subsidy_detail_information_url, 
            'description':subsidy_desc ,'application_period':subsidy_application_period ,'receving_agency' : subsidy_receiving_agency, 
            'telephone_inquiry': subsidy_telephone_inquiry,'support_type': subsidy_support_type,
            'application_process': subsidy_application_process,
            'application_process_url' : subsidy_application_process_url})
        print(id)
        id +=1 
    page_count += 12
    

with open(f'subsidy_data{start_page}~{end_page}.csv', 'w', newline='') as csvfile:
    fieldnames = ['id','title' ,'detail_information_url', 'description','application_period' ,'receving_agency', 'telephone_inquiry', 'support_type',  'application_process','application_process_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)

print(f"총 {len(data_list)}개의 데이터가 subsidy_data{start_page}~{end_page}.csv 파일에 저장되었습니다.")
    
        



    