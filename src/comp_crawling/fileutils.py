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
<<<<<<< HEAD:src/fileutils.py
        f.write(str[4:])
        print(path)
=======
        f.write(str)
>>>>>>> 7435f74f02fc5fe1791d29ce21c239ee654943d0:src/comp_crawling/fileutils.py

def write_into(directory):
    def wrapper(path, str):
        write_to_file(join(directory, path), str)
        return True
    return wrapper

def subfiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
