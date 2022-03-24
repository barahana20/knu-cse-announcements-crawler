import requests
from bs4 import BeautifulSoup
import os
import markdownify

def aa(tr_href, tr_bbs_num, tr_date):
  
  res = requests.get(tr_href)
  soup = BeautifulSoup(res.text, 'html.parser') 
  tr_title = soup.find('div', attrs={'class':'kboard-title'}).text
  tr_title = tr_title.replace('  ', ' ')
  # soup.
  # h = markdownify.markdownify(soup.currentTag, heading_style="ATX")
  h = markdownify.markdownify(res.text, heading_style="ATX")
  h = str(h)
  h = h.replace('/_files/userfile/image', 'https://computer.knu.ac.kr/_files/userfile/image')
  comp_link = 'https://computer.knu.ac.kr/06_sub/02_sub.html'
  h = h.replace('/pack/bbs/down.php', 'https://computer.knu.ac.kr/pack/bbs/down.php')
  h = h.replace('?key', comp_link+'?key')
  h = h.replace('?bbs_cmd', comp_link+'?bbs_cmd')
  with open(f'./storage/{str(tr_bbs_num)}_{tr_date}.md', 'w') as f:
      # print(h[h.index(tr_title):h.index("$(document).on('ready',function () {")])
    f.write(h[h.index(tr_title):h.index("$(document).on('ready',function () {")])
    
    # f.write(h)
  # print(h)