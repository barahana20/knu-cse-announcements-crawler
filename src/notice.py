from typing import Optional
from typing_extensions import assert_never
from lazy_property import LazyProperty

from datetime import datetime
import re as regex
import json

import requests
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup, Tag
from bs4.element import Tag as Element
from markdownify import markdownify


class Notice:
  '''
  Notice of KNU CSE official notice post
  example: https://computer.knu.ac.kr/06_sub/02_sub.html?no=3739&bbs_cmd=view
  '''
  post_url = 'https://computer.knu.ac.kr/06_sub/02_sub.html' 
  down_url = "https://computer.knu.ac.kr/pack/bbs/down.php"

  def __init__(self, url: str, is_announcement: bool = False):
    self.__url = url
    self.__is_announcement = is_announcement

    query = parse_qs(urlparse(url).query)
    self.id = int(query['no'])

  @LazyProperty
  def __soup(self) -> BeautifulSoup:
    response = requests.get(self.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
  
  @property
  def url(self) -> str:
    return f'{Notice.post_url}?no={self.id}&bbs_cmd=view'
  
  @property
  def title(self) -> str:
    title = self.__soup.find('div', attrs={'class': 'kboard-title'})
    return title.text
  
  @LazyProperty
  def timestamp(self) -> datetime:
    timestamp = (self.__soup
        .find('div', attrs={'class':'detail-attr detail-date'})
        .find('div', attrs={'class':'detail-value'}).text
    )
    return datetime.strptime(timestamp, '%Y-%m-%d %H:%M')

  @property
  def body(self) -> str:
    return self.__soup.find('div', attrs={'class':'content-view'}).text
  
  @property
  def is_announcement(self) -> bool:
    return self.is_announcement

  @property
  def has_mileage(self) -> bool:
    return '마일리지' in self.title or '마일리지' in self.body
  
  def to_markdown(self) -> str:
    '''
    convert Notice HTML code into markdown
    '''
    source = self.__soup.find('div', attrs={'id': 'kboard-document'})
    document = str(markdownify(source, heading_style="ATX"))
    document = (document
                .replace('/_files/userfile/image', 'https://computer.knu.ac.kr/_files/userfile/image')
                .replace('/pack/bbs/down.php', Notice.down_url)
                .replace('?key', Notice.post_url+'?key')
                .replace('?bbs_cmd', Notice.post_url+'?bbs_cmd')
                .replace(']첨부파일', ']  \n\n첨부파일') # 첨부파일 줄바꿈
               )

    for match in regex.finditer(r'o_name=.+?&', document):
      start, end = match.start(), match.end()
      document = document[:start] + document[start:end].replace(' ', '') + document[end:]
    
    return document

  def to_json(self) -> str:
    source = {
      self.id, self.title, self.timestamp, self.body
    }
    return json.dumps(source, indent=2, sort_keys=True)

  def __str__(self) -> str:
    return '\n'.join([
     f'url: {self.url}',
     f'\ttitle: {self.title[:10]}...',
     f'\tid: {self.id}',
     f'\ttimestamp: {self.timestamp}',
     f'\tbody: {self.body[:10]}...'
    ]).expandtabs(4)
  
  def __repr__(self) -> str:
    return '\n'.join([
     f'url: {self.url}',
     f'\ttitle: {self.title}...',
     f'\tid: {self.id}',
     f'\ttimestamp: {self.timestamp}',
     f'\tbody: {self.body}...'
    ]).expandtabs(4)


class NoticeFactory:
  '''
  Create Notice of KNU CSE official notice lists \n
  example: https://computer.knu.ac.kr/06_sub/02_sub.html
  '''
  @staticmethod
  def __from_notice_list_each(notice: Tag) -> 'Notice':
    '''
    create Notice from notice list in website \n
    example: https://computer.knu.ac.kr/06_sub/02_sub.html
    '''
    [span.extract() for span in notice.select('span')]
    url = Notice.post_url + notice.find('a')['href']
    is_announcement = notice.find('th', attrs={'class': 'bbs_num'}).text == '공지'
    return Notice(url, is_announcement)
    
  @staticmethod
  def from_notice_list() -> list['Notice']:
    '''
    create a list of Notice from the knu cse notice list \n
    example: https://computer.knu.ac.kr/06_sub/02_sub.html
    '''
    res = requests.get()
    soup = BeautifulSoup(res.text, 'html.parser')
    notices = soup.find_all('tr')  # 일반 공지사항 목록 가져옴

    return [NoticeFactory.__from_notice_list_each(notice) for notice in notices]
