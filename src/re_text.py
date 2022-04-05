import re

string = """첨부파일 : [붙임2. 학습스터디 안내.pdf](https://computer.knu.ac.kr/pack/bbs/down.php?f_name=QEdUVllEWFReVHlPcREYblNAQw==&o_name=붙임2. 학습스터디 안내.pdf&tbl=Site_BBS_25) [183 KB]첨부파일 : [붙임1. 2022학년도 1학기 첨성인 학습스터디 모집 안내.hwp](https://computer.knu.ac.kr/pack/bbs/down.php?f_name=Q0dUVllEWFReVHlPcREYbktTVQ==&o_name=붙임1. 2022학년도 1학기 첨성인 학습스터디 모집 안내.hwp&tbl=Site_BBS_25) [328 KB]"""
comp_down_link = r"https://computer.knu.ac.kr/pack/bbs/down.php"
c = re.compile(comp_down_link+r'.+Site_BBS_25')
a = re.findall(c, string)
print(a)