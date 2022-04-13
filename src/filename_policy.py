from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
from time import strftime, strptime
from typing import Tuple
from notice import Notice
from fileutils import to_allowed_filename


forbidden_to_allowed_chars = {
  '\\':'＼', '/':'／', ':':'：', '*':'＊', '?':'？', '"':'＂', '<':'＜', '>':'＞', '|':'｜', '.':'．'
}

def to_allowed_filename(string: str) -> str:
    '''
    change forbidden chars for filename into allowed chars
    '''
    for forbidden, allowed in forbidden_to_allowed_chars.items():
        string = string.replace(forbidden, allowed)
    return string


timestamp_format = '%Y-%m-%dT%H-%M' 

def notice_to_filename(notice: Notice) -> str:
  '''
  convert notice into filename 
  :return: formatted string: ('{id}_{title}_%Y-%m-%dT%H-%M')
  '''
  id = notice.id
  title = to_allowed_filename(notice.title)
  timestamp = strftime(notice.timestamp, timestamp_format)
  return f'{id}_{title}_{timestamp}'

@dataclass
class NoticeInfo:
  id: int
  title: str
  timestamp: datetime

def filename_to_notice_info(name: str) -> NoticeInfo:
  '''
  convert filename into notice info
  :return: id, title, timestamp
  '''
  tokens = name.split('_')
  id, title, datetime = tokens[0], tokens[1:-2], tokens[-1]
  return NoticeInfo(int(id), str.join('', title), strptime(datetime, timestamp_format))
