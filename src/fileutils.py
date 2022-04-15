from os import makedirs, listdir
from os.path import isfile, join

_forbidden_to_allowed_chars = {
  '\\':'＼', '/':'／', ':':'：', '*':'＊', '?':'？', '"':'＂', '<':'＜', '>':'＞', '|':'｜', '.':'．'
}

def createDir(directory):
    try:
        makedirs(directory, exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)
        
def to_allowed_filename(string):
    for forbidden, allowed in _forbidden_to_allowed_chars.items():
        string = string.replace(forbidden, allowed)
    return string

def write_to_file(path, str):
    with open(join(path), 'w', encoding='utf-8') as f:
        f.write(str[4:])
        print(path)

def write_into(directory):
    def wrapper(path, str):
        write_to_file(join(directory, path), str)
        return True
    return wrapper

def subfiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
