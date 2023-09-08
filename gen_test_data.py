import datetime
import random

COUNT_SMALL_DATA = 1000
COUNT_MEDIUM_DATA = 10000
COUNT_BIG_DATA = 100000
COUNT_HUGE_DATA = 1000000

dict_data_files = {COUNT_SMALL_DATA:'small_data.txt'
                    ,COUNT_MEDIUM_DATA:'medium_data.txt'
                    ,COUNT_BIG_DATA:'big_data.txt'
                    ,COUNT_HUGE_DATA:'huge_data.txt'
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
    print(f'{key} items generated in file {str(key) + "_" + value}', end='')
    gendata(key, str(key) + '_' + value)
    b = datetime.datetime.now()
    c = b - a
    print(f' during {c}')


