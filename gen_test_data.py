
import sys
import random

COUNT_SMALL_DATA = 1000
COUNT_MEDIUM_DATA = 10000
COUNT_BIG_DATA = 100000
COUNT_HUGE_DATA = 1000000

def gendata(max_size: int, filename: str) -> []:
    genset = set()
    genlist = []
    while len(genset) < max_size:
        number = random.randint(1, max_size)
        if number not in genset:
            genset.add(number)
            genlist.append(number)
    with open(filename, 'w', encoding='utf8') as f:
        f.write("%s " % len(genlist))
        for item in genlist:
            # write each item on a new line
            f.write("%s " % item)
    # return genlist

gotedlist = gendata(COUNT_SMALL_DATA,'small_data.txt')
gotedlist = gendata(COUNT_MEDIUM_DATA,'medium_data.txt')
gotedlist = gendata(COUNT_BIG_DATA,'big_data.txt')
gotedlist = gendata(COUNT_HUGE_DATA,'huge_data.txt')
