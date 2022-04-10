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
        print ('Error: Creating directory. ' +  directory)
        exit(1)

def get_cse_notices(comp_notice_url):
    res = requests.get(comp_notice_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    notices = soup.find_all('tr') # 일반 공지사항 목록 가져옴
    return notices

def is_announcement(notice):
    if(str(notice).find('bbs_num')!=-1):
        id = notice.find('td', attrs={'class':'bbs_num'}) # 공지사항 패스
        if(id != None): # 일반 공지인 경우 추가 탐색
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
    
    id = notice.find('td', attrs={'class':'bbs_num'}).text
    link = 'https://computer.knu.ac.kr/06_sub/02_sub.html' + notice.find('a')['href']
    date = notice.find('td', attrs={'class':'bbs_date'}).text.replace('-', '')
    return NoticeInfo(id, link, date)
    
def make_md(link, save_path):    
    res = requests.get(link)
    script_remove_compile = re.compile(r"s/<script.*<\/script>//g;/<script/,/<\/script>/{/<script/!{/<\/script>/!d}};s/<script.*//g;s/.*<\/script>//g\")
    print(re.findall(script_remove_compile, res.text))
    exit(1)
    soup = BeautifulSoup(res.text, 'html.parser') 
    title = soup.find('div', attrs={'class':'kboard-title'}).text
    title = title.replace('  ', ' ')
    comp_link = 'https://computer.knu.ac.kr/06_sub/02_sub.html'
    comp_down_link = "https://computer.knu.ac.kr/pack/bbs/down.php"
    h = markdownify.markdownify(res.text, heading_style="ATX")
    h = str(h)
    '''
    r"s/<script.*<\\/script>//g;/<script/,/<\\/script>/{/<script/!{/<\\/script>/!d}};s/<script.*//g;s/.*<\\/script>//g\"
    '''
    with open('./test.md', 'w', encoding='utf-8') as f:
        f.write(h)
    exit(1)
    if(h.find('마일리지')!=-1):
        print(id, '찾음')
    h = h.replace('/_files/userfile/image', 'https://computer.knu.ac.kr/_files/userfile/image')
    
    h = h.replace('/pack/bbs/down.php', comp_down_link)

    h = h.replace('?key', comp_link+'?key')
    h = h.replace('?bbs_cmd', comp_link+'?bbs_cmd')
    h = h[h.index(title):h.index("$(document).on('ready',function () {")]
    if(h.find(comp_down_link)!=-1):
        c = re.compile(comp_down_link+r'.+Site_BBS_25')
        a = re.findall(c, h) # 파일 다운로드 링크를 정규표현식으로 가져옴
    
        for a1 in a:
            h = h.replace(a1, a1.replace(' ', '')) # 파일명 공백 제거
        h = h.replace(']첨부파일', ']  \n\n첨부파일') # 첨부파일 줄바꿈
    
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(h)

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

    for notice in get_cse_notices(comp_notice_url.format(1)):
        if(is_announcement(notice)):
            continue
        id, link, date = get_info_from_notice(notice)
        make_md(link, './storage/{id}_{date}.md')
