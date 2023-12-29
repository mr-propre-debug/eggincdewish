import os

import json


class Data:
    
    with open("data/data.json", "ab+") as ab:
        ab.close()
        f = open('data/data.json','r+')
        f.readline()
        if os.stat("data/data.json").st_size == 0:
            f.write('{"money" : 0, "chickens" : 0, "eggs" : 0, "moneyMultiplier": 1, "eggLayingRate": 1}')
            f.close()
        else:
            pass
    def __init__(self):
        pass

    def getData():
        with open("data/data.json", 'r') as f:
            data = json.load(f)
        f.close()
        return data
    
    def save(DATA):
        with open('data/data.json', 'w') as f:
            json.dump(DATA, f)
        f.close()

    def manualSave(DATA):
        with open('data/data.json', 'w') as f:
            json.dump(DATA, f)
        f.close()
