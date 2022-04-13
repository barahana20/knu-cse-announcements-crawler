'''
함수형으로 코드를 짤려고 노력
    예시:
        공지들을 뽑아서
        일반 공지만 뽑은 다음
        공지에서 원하는 정보만 추출
        정보를 토대로 마크다운 문서 저장
    원칙:
        1. 하나의 함수는 하나의 역할만
        2. 함수는 side-effect 없이
        3. 타입은 일관되게
        4. 작명은 개념 중심, 주석은 기술 중심
        5. 더 간단하게 코드를 만들고 중복을 삭제하기

storage/년/월 디렉토리를 만들고
"번호_제목_%Y-%m-%dT%H:%M"으로 각 공지사항 파일을 만들어서
마크다운으로 변환하여 저장
갱신할 때는 해당 월 디렉토리 안에서 가장 최신(년월일이 가장 높은 파일)인 파일을 찾음
'''

"""
1. 새로운 공지사항을 발견했을 때 등록된 사용자 이메일로 메일을 보냄
2. 모든 올라오는 공지사항을 저장후 최근 1주일 간의 데이터들과 마일리지 정보들을 카카오톡 챗봇에게 요청하면 그것들을 출력함.
"""

from notice import Notice, NoticeFactory
from fileutils import write_into, subfiles, createDir
from filename_policy import NoticeInfo, notice_to_filename, filename_to_notice_info

if __name__ == '__main__':
    pass
