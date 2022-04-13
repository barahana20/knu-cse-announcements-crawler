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
<<<<<<< HEAD
        f.write(replace_easy_visually(str))
=======
        f.write(str)
>>>>>>> cb970c7e5202a2339ccead7379cfd409714191e7

def write_into(directory):
    def wrapper(path, str):
        write_to_file(join(directory, path), str)
    return wrapper

def subfiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
