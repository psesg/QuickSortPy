def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    # Find the last index for each element
    c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result


def count_sort(alist, num_sorted_items_print):
    arr_sorted = counting_sort(alist, max(alist))
    if num_sorted_items_print > 0:
        print(f'\t{list(arr_sorted[:num_sorted_items_print])}', end='')
    return arr_sorted
