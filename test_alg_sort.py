# Some sort alg in Python

# importing libraries

import array as arr
from numpy import *
from const import *

from util import *
from quick_sort import *
from bubble_sort import *
from selection_sort import *
from insertion_sort import *
from merge_sort import *

list_data_files = ['small_data.txt'
    , 'medium_data.txt'
    # , 'big_data.txt'
                   # ,'huge_data.txt'
                   ]
dict_items_count = {'small_data.txt': COUNT_SMALL_DATA
    , 'medium_data.txt': COUNT_MEDIUM_DATA
    , 'big_data.txt': COUNT_BIG_DATA
    , 'huge_data.txt': COUNT_HUGE_DATA
                    }


def alg_inter_sort(array):
    print('\talg_inter_sort: ', end='')
    sorted(array)


def alg_quick_sort(array):
    print('\talg_sort_quick: ', end='')
    quick_sort(array, 0, len(array) - 1)


def alg_merge_sort(array):
    print('\talg_merge_sort: ', end='')
    merge_sort(array)


def alg_select_sort(array):
    print('\talg_select_sort: ', end='')
    selection_sort(array)


def alg_insert_sort(array):
    print('\talg_insert_sort: ', end='')
    insertion_sort(array)


def alg_bubble_sort(array):
    print('\talg_bubble_sort: ', end='')
    bubble_sort(array)


func_list = [alg_inter_sort, alg_quick_sort, alg_merge_sort, alg_select_sort,
             alg_insert_sort, alg_bubble_sort]



@calculate_time
def run_alg(array, f):
    f(array)


for data_file in list_data_files:
    print(f'got {dict_items_count[data_file]} unsorted items form {data_file}')
    for f in func_list:
        # Создание массива
        int_arr = arr.array('i')
        fl = open(data_file, encoding='utf8')
        big_str = fl.readline().strip("\n")
        fl.close()
        # big_str = sys.stdin.readline().strip("\n")
        big_strips = big_str.split(' ')
        ncount = int(big_strips[0])
        for i in range(1, ncount + 1):
            int_arr.append(int(big_strips[i]))
        run_alg(int_arr, f)
