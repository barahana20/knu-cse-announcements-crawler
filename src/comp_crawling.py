import requests
from bs4 import BeautifulSoup
import os
import markdown_func

URL = "https://computer.knu.ac.kr/06_sub/02_sub.html?page=%s&key=&keyfield=&category=&bbs_code=Site_BBS_25"

def createDir(directory):
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        return False

"""
storage 디렉토리를 만들고
"번호.제목"으로 각 공지사항 폴더을 만들어서
마크다운으로 변환하여 저장
"""

if __name__ == '__main__':
    if createDir('./storage'):
        pass
    else:
        exit(1)
    
    res = requests.get(URL % 1)
    soup = BeautifulSoup(res.text, 'html.parser')
    tr_boxes = soup.find_all('tr')

    for tr_box in tr_boxes:
        if(str(tr_box).find('bbs_num')!=-1):
            # 거르는 함수, 필요한 데이터를 뽑아서 튜플이나 딕셔너리나 soup로 감싸 반환하는 함수 , markdown.md에 넣는 함수 만들기
            tr_bbs_num = tr_box.find('td', attrs={'class':'bbs_num'}) # 공지사항 패스
            if(tr_bbs_num != None): # 일반 공지인 경우 추가 탐색
                tr_bbs_num = tr_bbs_num.text
                if(str(tr_box).find('font')!=-1):
                    tr_title = tr_box.find('font').text
                else:
                    tr_title = tr_box.find('a', {}).text
                tr_href = 'https://computer.knu.ac.kr/06_sub/02_sub.html'+tr_box.find('a')['href']
                tr_writer = tr_box.find('td', attrs={'class':'bbs_writer'}).text
                tr_date = tr_box.find('td', attrs={'class':'bbs_date'}).text.replace('-', '')
                markdown_func.aa(tr_href, tr_bbs_num, tr_date)
                # print(tr_bbs_num)
                # print(tr_href)
                # print(tr_title)
                # print(tr_writer)
                # print(tr_date)
        # else:
        #     print('페이지에 아무것도 없어 종료합니다.')
        #     break # 아예 뭐가 없으면 끝까지 탐색한 것으로 생각하고 종료