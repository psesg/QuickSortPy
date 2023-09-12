import datetime
import random
from const import *

dict_data_files = {DATA_1000: str(DATA_1000) + '.txt'
                    ,DATA_10000: str(DATA_10000) + '.txt'
                    ,DATA_15000: str(DATA_15000) + '.txt'
                    ,DATA_50000: str(DATA_50000) + '.txt'
                   }
def gendata(max_size: int, filename: str) -> []:
    genset = set()
    genlist = []
    while len(genset) < max_size:
        number = random.randint(1, max_size)
        if number not in genset:
            genset.add(number)
            genlist.append(number)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(f'{len(genlist)} ')
        for item in genlist:
            # write each item on a new line
            f.write(f'{item} ')

for key, value in dict_data_files.items():
    a = datetime.datetime.now()
    print(f'{key} items generated in file {value}', end='')
    gendata(key, value)
    b = datetime.datetime.now()
    c = b - a
    print(f' during {c}')


