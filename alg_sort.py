# Some sort in Python

import datetime
import array as arr

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


outlist = []
# Создание массива
int_arr = arr.array('i')
int_arr1 = arr.array('i')
f = open('100000_big_data.txt', encoding='utf8')
big_str = f.readline().strip("\n")
f.close()
# big_str = sys.stdin.readline().strip("\n")
big_strips = big_str.split(' ')
ncount = int(big_strips[0])
for i in range(1, ncount+1):
    int_arr.append(int(big_strips[i]))
    int_arr1.append(int(big_strips[i]))

print("Got unsorted Array")
# print(inputlist)

size = len(int_arr)
a = datetime.datetime.now()
quickSort(int_arr, 0, size - 1)
b = datetime.datetime.now()
c = b - a
newsize = len(int_arr)
print('QuickSorted int Array length = {} in {}: '.format(newsize, c))

size = len(int_arr1)
a = datetime.datetime.now()
outlist = sorted(int_arr1)
b = datetime.datetime.now()
c = b - a
newsize = len(int_arr1)
print('Sorted internal function Array length = {} in {}: '.format(newsize, c))
# print(outlist)
