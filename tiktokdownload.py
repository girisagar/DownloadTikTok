import os
import sys
import time
import json
import requests
import traceback
from urllib.parse import urlparse

class TiktokStore():
    def __init__(self, destdir):
        self.destdir = destdir.rstrip('/')

    def get_mime_type(self, uri):
        for item in uri.query.split('&'):
            item_map = item.split('=')
            if len(item_map) > 1:
                key, value = item_map[0], item_map[1]
                if key == 'mime_type':
                    mime_type = value.strip('video').strip('_')
                    print("found", mime_type)
                    return mime_type
        print("MimeType Not Found!!", uri)
        return 

    def download_video_series(self, index, link):
        # obtain filename by splitting url and getting
        # last string
        link_uri = urlparse(link)
        mime_type = self.get_mime_type(link_uri) 
        prefix = link_uri.path.split('/')[-1]
        file_name = f"{self.destdir}/{index}_{prefix}"
        if mime_type:
            file_name = f"{file_name}.{mime_type}"
        print(f"Downloading file: {file_name}")
        # create response object
        r = requests.get(link, stream = True)
        
        # start downloading files
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)
        
        print(f"{file_name} downloaded!")
        return

if __name__ == "__main__":
    file_name = sys.argv[1]
    destdir = sys.argv[2]
    data = json.load(open(file_name))
    not_found = []
    errors = []
    store = TiktokStore(destdir)
    for index in range(len(data['Video']['Videos']['VideoList'])):
        print('\n-------------------------------------------------')
        tiktok_url = data['Video']['Videos']['VideoList'][index]['Link']
        try:
            store.download_video_series(index, tiktok_url)
        except Exception as e:
            print(f"ERROR!!: {e}")
            errors.append(traceback.format_exc())
            not_found.append((index, tiktok_url))
        time.sleep(2)
    if len(not_found) > 0:
        print("Couldn't download videos for these links")
        for nf in not_found:
            print(nf)

