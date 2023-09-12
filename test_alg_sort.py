# Some sort alg in Python

# importing libraries

import array as arr
import copy

from const import *

from util import *
from alg_quick_sort import *
from alg_bubble_sort import *
from alg_selection_sort import *
from alg_insertion_sort import *
from alg_merge_sort import *
from alg_heap_pyr_sort import *
from alg_counting_sort import *
from alg_radix_sort import *

# TODO: enhance
#   NOT! Slowly up to 5 tomes! In gen_test_data not need use set,  just list.
#   NOT! slowly up to 2 times! Make arrays as  numpy array.
#   Made_OK! Code  function for  take time transfer to util.py
#   Made_OK! Read one set from file at once, then sort just copy of array.
#   Made_OK! All sort function return list and print SORTED_DATA_SAMPLE items.
#   https://stackoverflow.com/questions/37593013/deep-copy-of-a-np-array-of-np-array
# 	https://www.geeksforgeeks.org/array-copying-in-python/

dict_data_files = {}
for d_file in data_file_list:
    dict_data_files.update({d_file: str(d_file) + '.txt'})

def alg_inter_sort(array, num_sorted_items_print=0):
    print('\talg_inter_sort: ', end='')
    sorted_arr = sorted(array)
    if num_sorted_items_print > 0:
        print(f'\t{list(sorted_arr[:num_sorted_items_print])}', end='')


def alg_quick_sort(array, num_sorted_items_print=0):
    print('\talg_sort_quick: ', end='')
    quick_sort_wrap(array, 0, len(array) - 1, num_sorted_items_print)


def alg_merge_sort(array, num_sorted_items_print=0):
    print('\talg_merge_sort: ', end='')
    merge_sort_wrap(array, num_sorted_items_print)


def alg_select_sort(array, num_sorted_items_print=0):
    print('\talg_select_sort: ', end='')
    selection_sort(array, num_sorted_items_print)


def alg_insert_sort(array, num_sorted_items_print=0):
    print('\talg_insert_sort: ', end='')
    insertion_sort(array, num_sorted_items_print)


def alg_bubble_sort(array, num_sorted_items_print=0):
    print('\talg_bubble_sort: ', end='')
    bubble_sort(array, num_sorted_items_print)

def alg_heap_pyr_sort(array, num_sorted_items_print=0):
    print('\talg_heap_pyr_sort: ', end='')
    heapsort(array, num_sorted_items_print)


def alg_count_sort(array, num_sorted_items_print=0):
    print('\talg_count_sort: ', end='')
    count_sort(array, num_sorted_items_print)


def alg_radix_sort(array, num_sorted_items_print=0):
    print('\talg_radix_sort: ', end='')
    radix_sort(array, num_sorted_items_print)


#
func_list = [alg_inter_sort, alg_count_sort, alg_radix_sort,
             alg_quick_sort, alg_merge_sort, alg_heap_pyr_sort,
             alg_select_sort, alg_insert_sort, alg_bubble_sort,
             ]


@calculate_time
def run_alg(array, f):
    f(array, SORTED_DATA_SAMPLE)

for k, v in dict_data_files.items():
    print(f'got {k} unsorted items form {v}')
    int_arr_org = arr.array('i')
    fl = open(v, encoding='utf8')
    big_str = fl.readline().strip("\n")
    fl.close()
    # big_str = sys.stdin.readline().strip("\n")
    big_strips = big_str.split(' ')
    ncount = int(big_strips[0])
    for i in range(1, ncount + 1):
        int_arr_org.append(int(big_strips[i]))
    for f in func_list:
        # копироваие массива для тестирования
        int_arr_tst = copy.deepcopy(int_arr_org)
        run_alg(int_arr_tst, f)
