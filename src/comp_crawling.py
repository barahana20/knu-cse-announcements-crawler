import os
import re as regex
from collections import namedtuple
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
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

def into_filename(notice):
    _, id, title, timestamp, _ = notice
    timestamp = timestamp.strftime("%Y-%m-%dT%H-%M")
    return to_allowed_filename(f'{id}_{title}_{timestamp}')+'.md'

def make_md(source):
    comp_link = 'https://computer.knu.ac.kr/06_sub/02_sub.html'
    comp_down_link = "https://computer.knu.ac.kr/pack/bbs/down.php"
    
    document = str(markdownify(str(source), heading_style="ATX"))
    document = (document
                .replace('/_files/userfile/image', 'https://computer.knu.ac.kr/_files/userfile/image')
                .replace('/pack/bbs/down.php', comp_down_link)
                .replace('?key', comp_link+'?key')
                .replace('?bbs_cmd', comp_link+'?bbs_cmd')
                .replace(']첨부파일', ']  \n\n첨부파일') # 첨부파일 줄바꿈
               )

    for match in regex.finditer(r'o_name=.+?&', document):
        start, end = match.start(), match.end()
        document = document[:start] + document[start:end].replace(' ', '') + document[end:]

    return document

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

    info_to_filename_and_makrdown = lambda info: (into_filename(info), make_md(info.source))
    write_to_storage = lambda filename_and_document: write_into(storage_path)(*filename_and_document)

    notices = get_cse_notices(comp_notice_url.format('1'))
    (seq(notices)
        .filter_not(is_announcement)
        .map(get_info_from_notice)
        .map(info_to_filename_and_makrdown)
        .for_each(write_to_storage)
    )
    
    '''
    for notice in get_cse_notices(comp_notice_url.format(1)):
        if(is_announcement(notice)):
            continue
        id, link, date = get_info_from_notice(notice)
        make_md(link, f'{id}_{date}.md', storage_path, mile_path)
    '''