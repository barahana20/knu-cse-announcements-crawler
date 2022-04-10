import requests
from bs4 import BeautifulSoup
import os
import markdownify
import re
def aa(tr_href, tr_bbs_num, tr_date):
  
  res = requests.get(tr_href)
  soup = BeautifulSoup(res.text, 'html.parser') 
  tr_title = soup.find('div', attrs={'class':'kboard-title'}).text
  tr_title = tr_title.replace('  ', ' ')
  # soup.
  # h = markdownify.markdownify(soup.currentTag, heading_style="ATX")
  h = markdownify.markdownify(res.text, heading_style="ATX")
  h = str(h)
  # print(h)
  # exit(1)
  h = h.replace('/_files/userfile/image', 'https://computer.knu.ac.kr/_files/userfile/image')
  comp_link = 'https://computer.knu.ac.kr/06_sub/02_sub.html'
  comp_down_link = "https://computer.knu.ac.kr/pack/bbs/down.php"
  h = h.replace('/pack/bbs/down.php', comp_down_link)
  
  h = h.replace('?key', comp_link+'?key')
  h = h.replace('?bbs_cmd', comp_link+'?bbs_cmd')
  h = h[h.index(tr_title):h.index("$(document).on('ready',function () {")]
  if(h.find(comp_down_link)!=-1):
    c = re.compile(comp_down_link+r'.+Site_BBS_25')
    a = re.findall(c, h)
    print(a)
    for a1 in a:
      # print(a1)
      pass
    exit(1)
  exit(1)
  # with open(f'./storage/{str(tr_bbs_num)}_{tr_date}.md', 'w') as f:
      # 
    # f.write(h[h.index(tr_title):h.index("$(document).on('ready',function () {")])
    
    # f.write(h)
  # print(h)