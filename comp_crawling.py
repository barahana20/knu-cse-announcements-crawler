import requests
from bs4 import BeautifulSoup
import os

URL = "https://computer.knu.ac.kr/06_sub/02_sub.html?page=%s&key=&keyfield=&category=&bbs_code=Site_BBS_25"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
"""
storage 디렉토리를 만들고
"번호.제목"으로 각 공지사항 폴더을 만들어서
마크다운로

"""

# if __name__ == '__main__':
#     res = requests.get(URL % 1)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     print(soup)
#     pass
