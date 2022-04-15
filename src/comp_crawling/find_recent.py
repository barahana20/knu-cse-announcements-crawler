from datetime import datetime

def find_recent(file_name, new_timestamp):
    timestamp = file_name[file_name.rfind('_')+1:file_name.index('.md')]
    timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H-%M")
    new_timestamp = datetime.strptime(new_timestamp, "%Y-%m-%dT%H-%M")

    if timestamp < new_timestamp:
        return True
    else:
        return False

if find_recent(r'{info.id}_{info.title}_2022-04-07T01-22.md', '2023-04-07T01-22'):
    print('새로 가져온 파일이 더 최신입니다.')