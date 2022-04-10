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

  h = markdownify.markdownify(res.text, heading_style="ATX")
  h = str(h)
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
    for a1 in a:
      h = h.replace(a1, a1.replace(' ', ''))
    h = h.replace(']첨부파일', ']\n첨부파일')
  with open(f'./storage/{str(tr_bbs_num)}_{tr_date}.md', 'w', encoding='utf-8') as f:
    f.write(h)