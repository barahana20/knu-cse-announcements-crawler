import requests
from bs4 import BeautifulSoup
import re
import datetime as dt

# c = re.compile()
res = requests.get('https://computer.knu.ac.kr/06_sub/02_sub.html?no=3739&bbs_cmd=view&page=1&key=&keyfield=&category=&bbs_code=Site_BBS_25')
soup = BeautifulSoup(res.text, 'html.parser')

timestamp = (soup
    .find('div', attrs={'class':'detail-attr detail-date'})
    .find('div', attrs={'class':'detail-value'}).text
    )
timestamp = dt.datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
print(timestamp.date())
print(timestamp.day)
print(timestamp.year)
print(timestamp.month)
print(timestamp.time())
# print(timestamp.replace(' ', '').replace('-', '').replace(':', ''))
