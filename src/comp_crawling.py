import os
import re as regex
from collections import namedtuple
import requests
from bs4 import BeautifulSoup
import markdownify
from functional import seq
from fileutils import *
from datetime import datetime
from urllib.parse import unquote

comp_notice_url = "https://computer.knu.ac.kr/06_sub/02_sub.html?page={}&key=&keyfield=&category=&bbs_code=Site_BBS_25"
storage_path = './storage'
mile_path = './mile'
NoticeInfo = namedtuple('NoticeInfo', 'link id title timestamp source')

def get_cse_notices(comp_notice_url):
    res = requests.get(comp_notice_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    notices = soup.find_all('tr')  # 일반 공지사항 목록 가져옴
    
    return notices

def is_announcement(notice):
    if(str(notice).find('bbs_num') != -1):
        id = notice.find('td', attrs={'class': 'bbs_num'})  # 공지사항 패스
        if(id != None):  # 일반 공지인 경우 추가 탐색
            return False
    return True

def get_info_from_notice(notice):
    """
    #  글 제목, 글 작성자
    if(str(notice).find('font')!=-1):
        print('정상작동')
        title = notice.find('font').text
    else:
        print('에러')
    
    writer = notice.find('td', attrs={'class':'bbs_writer'}).text
    """
    [span.extract() for span in notice.select('span')]
    
    id = notice.find('td', attrs={'class': 'bbs_num'}).text
    title = notice.find('a').text.strip()
    link = 'https://computer.knu.ac.kr/06_sub/02_sub.html' + notice.find('a')['href']
    
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')

    source = soup.find('div', attrs={'id': 'kboard-document'})
    timestamp = (soup
        .find('div', attrs={'class':'detail-attr detail-date'})
        .find('div', attrs={'class':'detail-value'}).text
    )
    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    
    return NoticeInfo(link, id, title, timestamp, source)

def make_md(source, filename, storage_path, mile_path):
    comp_link = 'https://computer.knu.ac.kr/06_sub/02_sub.html'
    comp_down_link = "https://computer.knu.ac.kr/pack/bbs/down.php"

    document = (str(source)
                .replace('/_files/userfile/image', 'https://computer.knu.ac.kr/_files/userfile/image')
                .replace('/pack/bbs/down.php', comp_down_link)
                .replace('?key', comp_link+'?key')
                .replace('?bbs_cmd', comp_link+'?bbs_cmd')
                .replace(']첨부파일', ']  \n\n첨부파일') # 첨부파일 줄바꿈
               )
    """
    href="/pack/bbs/down.php?f_name=Q0dUVllEWVdbVHZLcRUQblNAQw==&o_name=2022년 GKS 외국인 우수 자비 장학생 모집 공고(안내용).pdf&tbl=Site_BBS_25"
    """
    for match in regex.finditer(r'o_name=.+?"', document):
        start, end = match.start(), match.end()
        document = document[:start] + document[start:end].replace(' ', '') + document[end:]

    return document
    
    with open(os.path.join(storage_path, filename), 'w', encoding='utf-8') as f:
        f.write(document)

    if '마일리지' in document:
        with open(os.path.join(mile_path, filename), 'w', encoding='utf-8') as f:
            f.write(document)

'''
함수형으로 코드를 짤려고 노력
    예시:
        공지들을 뽑아서
        일반 공지만 뽑은 다음
        공지에서 원하는 정보만 추출
        정보를 토대로 마크다운 문서 저장
    원칙:
        1. 하나의 함수는 하나의 역할만
        2. 함수는 side-effect 없이
        3. 타입은 일관되게
        4. 작명은 개념 중심, 주석은 기술 중심
        5. 더 간단하게 코드를 만들고 중복을 삭제하기

storage/년/월 디렉토리를 만들고
"번호_제목_%Y-%m-%dT%H:%M"으로 각 공지사항 파일을 만들어서
마크다운으로 변환하여 저장
갱신할 때는 해당 월 디렉토리 안에서 가장 최신(년월일이 가장 높은 파일)인 파일을 찾음
'''

if __name__ == '__main__':
    createDir(storage_path)
    createDir(mile_path)

    is_not_announcement = lambda notice: not is_announcement(notice)
    make_md_by_info = lambda info: make_md(info.source, f'{info.id}_{to_allowed_filename(info.title)}_{info.timestamp.strftime("%Y-%m-%dT%H:%M")}.md', storage_path, mile_path)

    notices = get_cse_notices(comp_notice_url.format('1'))
    first3 = (seq(notices)
        .filter(is_not_announcement)
        .map(get_info_from_notice)
        .map(make_md_by_info)
        .take(3)
         #.to_list()
    )
    
    for i, f in enumerate(first3):
        write_to_file(f'example{i}.md', f)

    '''
    for notice in get_cse_notices(comp_notice_url.format(1)):
        if(is_announcement(notice)):
            continue
        id, link, date = get_info_from_notice(notice)
        make_md(link, f'{id}_{date}.md', storage_path, mile_path)
    '''