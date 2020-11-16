import requests
import json
from pathlib import Path
import csv
from threading import Thread

MY_FILE = Path("qrng.csv")
ARRAY = []
BUSY = 0

class DownloadThread(Thread):

    def __init__(self, url, name, busy):
        """Init"""
        Thread.__init__(self)
        self.name = name
        self.url = url
        self.busy = busy


    def run(self):
        response = requests.get(self.url)
        json_str = json.dumps(response.json())
        data = json.loads(json_str)
        row = data['data']
        # print(row)
        ARRAY.append(row)
        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        d = len(ARRAY)
        print(msg + " - " + str(d))
        if len(ARRAY) == 10:
            print(ARRAY)


def process(url, count):
    b = BUSY
    b = 0
    c = count
    while c != 0:
        # print(c)
        c = c - 1
        name = "Поток %s" % c
        thread = DownloadThread(url, name)
        thread.start()



if __name__ == '__main__':
    VAL = 10
    URL = 'https://qrng.anu.edu.au/API/jsonI.php?length=10&type=uint8'
    process(URL, VAL)
