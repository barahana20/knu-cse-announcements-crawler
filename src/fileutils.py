from os import makedirs, listdir
from os.path import isfile, join

def createDir(directory):
    try:
        makedirs(directory, exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)
        
def write_to_file(path, str):
    with open(join(path), 'w', encoding='utf-8') as f:
        f.write(str)

def write_into(directory):
    def wrapper(path, str):
        write_to_file(join(directory, path), str)
    return wrapper

def subfiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
