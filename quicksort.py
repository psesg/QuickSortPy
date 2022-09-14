# Quick sort in Python

import sys
import datetime
import random

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


inputlist = []
big_str = sys.stdin.readline().strip("\n")
big_strips = big_str.split(' ')
ncount = int(big_strips[0])
for i in range(1, ncount+1):
    inputlist.append(int(big_strips[i]))

print("Got unsorted Array")
# print(inputlist)

size = len(inputlist)
a = datetime.datetime.now()
quickSort(inputlist, 0, size - 1)
b = datetime.datetime.now()
c = b - a
newsize = len(inputlist)
print('Sorted int Array length = {} in {}: '.format(newsize, c))
# print(inputlist)
