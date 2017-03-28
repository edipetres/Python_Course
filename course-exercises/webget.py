import urllib.request
import os
from urllib.parse import urlparse

def download(url, path = './'):
    filename = os.path.basename(urlparse(url).path)
    print("Filename: " + filename)
    if(os.path.isfile(filename)):
        print("File found at " + path + " as " + filename)
    else:
        print("File not found; downloading...")
        fullfilename = os.path.join(path, filename)
        file_name, headers = urllib.request.urlretrieve(url, fullfilename)
        print("File saved to " + path + " as " + filename)
