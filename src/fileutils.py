import os

def createDir(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)

def 
