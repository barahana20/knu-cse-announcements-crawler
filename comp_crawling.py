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
마크다운으로 변환하여 저장

"""
if __name__ == '__main__':
    res = requests.get(URL % 1)
    soup = BeautifulSoup(res.text, 'html.parser')
    tr_boxes = soup.find_all('tr')
    count = 1
    for tr_box in tr_boxes:
        if(str(tr_box).find('bbs_num')!=-1):
            bbs_num = tr_box.find('td', attrs={'class':'bbs_num'})
            href = tr_box.find('a')['href']
            if(bbs_num != None):
                print(bbs_num.text)
                print(href)
                # with open(f"temp/{str(count)}", 'w') as f:
                #     f.write(str(tr_box))
        # count+=1
