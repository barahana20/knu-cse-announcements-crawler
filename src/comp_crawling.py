import requests
from bs4 import BeautifulSoup
import os
from collections import namedtuple
import markdownify
import re

comp_notice_url = "https://computer.knu.ac.kr/06_sub/02_sub.html?page={}&key=&keyfield=&category=&bbs_code=Site_BBS_25"

NoticeInfo = namedtuple('NoticeInfo', 'id link date')

def createDir(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)

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
    ''' 글 제목, 글 작성자
    if(str(notice).find('font')!=-1):
        print('정상작동')
        title = notice.find('font').text
    else:
        print('에러')
        title = notice.find('a', {}).text
    writer = notice.find('td', attrs={'class':'bbs_writer'}).text
    '''
    id = notice.find('td', attrs={'class': 'bbs_num'}).text
    link = 'https://computer.knu.ac.kr/06_sub/02_sub.html' + \
        notice.find('a')['href']
    date = notice.find('td', attrs={'class': 'bbs_date'}).text.replace('-', '')
    return NoticeInfo(id, link, date)

def into_link_and_filename(notice_info):
    id, link, date = notice_info
    return link, f'{id}_{date}.md'

def make_md(link, filename, storage_path, mile_path):
    comp_link = 'https://computer.knu.ac.kr/06_sub/02_sub.html'
    comp_down_link = "https://computer.knu.ac.kr/pack/bbs/down.php"

    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    elem = soup.find('div', attrs={'id': 'kboard-document'})

    document = str(markdownify.markdownify(str(elem), heading_style="ATX"))

    document = (document
                .replace('/_files/userfile/image', 'https://computer.knu.ac.kr/_files/userfile/image')
                .replace('/pack/bbs/down.php', comp_down_link)
                .replace('?key', comp_link+'?key')
                .replace('?bbs_cmd', comp_link+'?bbs_cmd')
                .replace(']첨부파일', ']  \n\n첨부파일') # 첨부파일 줄바꿈
               )
    
    if comp_down_link in document:
        c = re.compile(comp_down_link+r'.+Site_BBS_25')
        a = re.findall(c, document)  # 파일 다운로드 링크를 정규표현식으로 가져옴
        for a1 in a:
            document = document.replace(a1, a1.replace(' ', ''))  # 파일명 공백 제거

    with open(os.path.join(storage_path, filename), 'w', encoding='utf-8') as f:
        f.write(document)

    if '마일리지' in document:
        with open(os.path.join(mile_path, filename), 'w', encoding='utf-8') as f:
            f.write(document)

'''
공지들을 뽑아서
일반 공지만 뽑은 다음
공지에서 원하는 정보만 추출
'''
"""
storage 디렉토리를 만들고
"번호.올라온날짜"으로 각 공지사항 폴더을 만들어서
마크다운으로 변환하여 저장
"""
if __name__ == '__main__':
    createDir('./storage')
    createDir('./mile')
    
    for notice in get_cse_notices(comp_notice_url.format(1)):
        if(is_announcement(notice)):
            continue
        id, link, date = get_info_from_notice(notice)
        make_md(link, f'{id}_{date}.md', './storage', './mile')