import os

_forbidden_to_allowed_chars = {
  '\\':'＼', '/':'／', ':':'：', '*':'＊', '?':'？', '"':'＂', '<':'＜', '>':'＞', '|':'｜', '.':'．'
}

def createDir(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)
        
def to_allowed_filename(string):
    for forbidden, allowed in _forbidden_to_allowed_chars.items():
        string = string.replace(forbidden, allowed)
    return string

def write_to_file(path, str):
    with open(os.path.join(path), 'w', encoding='utf-8') as f:
        f.write(str)
  
  