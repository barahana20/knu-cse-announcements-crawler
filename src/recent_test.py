import glob, os, datetime

def get_recent_timestamp():
    datas = glob.glob('./storage/*')
    timestamp = []
    for data in datas:
        name = os.path.basename(data)
        
        timestamp.append(datetime.datetime.strptime(name[name.rfind('_')+1:name.index('.md')], "%Y-%m-%dT%H-%M"))
    return sorted(timestamp, reverse=True)[0]