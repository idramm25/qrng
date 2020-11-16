import requests
import json
from pathlib import Path
import csv
import time

URL = 'https://qrng.anu.edu.au/API/jsonI.php?length=256&type=uint8'
VAL = 256
MY_FILE = Path("qrng.csv")


def getjson():
    response = requests.get(URL)
    return response.json()


def getstring():
    json_str = json.dumps(getjson())
    data = json.loads(json_str)
    return data['data']


def writecsv():
    if MY_FILE.is_file():
        f = open(MY_FILE, "w+")
        f.close()
    with open('qrng.csv', 'w', newline='') as file:
        cursor = csv.writer(file)
        i = VAL
        while i != 1:
            cursor.writerow(getstring())
            string = ''.join(str(x) for x in getstring())
            print(str(i) + ' - ' + string)
            # time.sleep(1)
            i = i - 1
        return 'OK'


if __name__ == '__main__':
    # print(writecsv())
    print(getstring())