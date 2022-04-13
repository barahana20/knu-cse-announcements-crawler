from os import makedirs, listdir
from os.path import isfile, join

def createDir(directory):
    try:
        makedirs(directory, exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)

def write_to_file(path, str):
    replace_easy_visually = lambda x: x.replace('\n\n\n\n', '\n\n').replace('\n\n\n\n\n', '\n\n')
    with open(join(path), 'w', encoding='utf-8') as f:
        f.write(replace_easy_visually(str))

def write_into(directory):
    def wrapper(path, str):
        write_to_file(join(directory, path), str)
    return wrapper

def subfiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
