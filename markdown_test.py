import markdownify
import requests
from bs4 import BeautifulSoup
import os

URL = "https://computer.knu.ac.kr/06_sub/02_sub.html?no=3676&bbs_cmd=view&page=1&key=&keyfield=&category=&bbs_code=Site_BBS_25"

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser') 
# soup.
# h = markdownify.markdownify(soup.currentTag, heading_style="ATX")
h = markdownify.markdownify(res.text, heading_style="ATX")
h.replace('_files/userfile/image', 'http://cse.knu.ac.kr/_files/userfile/image')
with open('./markdown_test.md', 'w') as f:
  f.write(h)
print(h)
exit(1)
