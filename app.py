import requests
import json
from pathlib import Path
import csv
from threading import Thread

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



MY_FILE = Path("qrng.csv")
ARRAY = []
BUSY = 0

class DownloadThread(Thread):

    def __init__(self, url, name, count, busy):
        """Init"""
        Thread.__init__(self)
        self.name = name
        self.url = url
        self.count = count
        self.busy = busy


    def run(self):
        response = requests.get(self.url)
        json_str = json.dumps(response.json())
        data = json.loads(json_str)
        row = data['data']
        # print(row)
        ARRAY.append(row)
        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        # d = len(ARRAY)
        # print(msg + " - " + str(d))
        print(msg)
        if len(ARRAY) == self.count:
            BUSY = 0
            return


def plot():
    while BUSY != 0:
        pass
    print("OK")
    sns.heatmap(ARRAY, cmap="binary_r")
    plt.show()


def process(url, count):
    BUSY = 1
    while count != 0:
        # print(c)
        count = count - 1
        name = "Поток %s" % count
        thread = DownloadThread(url, name, BUSY, count)
        thread.start()
        s = str(count)
        print("Thread " + s + " started.")

    plot()



if __name__ == '__main__':
    VAL = 300
    URL = 'https://qrng.anu.edu.au/API/jsonI.php?length=300&type=uint8'
    process(URL, VAL)
