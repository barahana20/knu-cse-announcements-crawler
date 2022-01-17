import markdownify
import requests
from bs4 import BeautifulSoup
import os

URL = "https://computer.knu.ac.kr/06_sub/02_sub.html?page=%s&key=&keyfield=&category=&bbs_code=Site_BBS_25"

res = requests.get(URL % 1)
soup = BeautifulSoup(res.text, 'html.parser') 
# soup.
# h = markdownify.markdownify(soup.currentTag, heading_style="ATX")
h = markdownify.markdownify(res.text, heading_style="ATX")
with open('./markdown_test', 'w') as f:
  f.write(h)
print(h)
exit(1)
