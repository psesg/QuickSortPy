import operator


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr, compare):
    if len(arr) < 2:
        result = arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        result = merge(left, right, compare)
    return result

def merge_sort_wrap(arr, num_sorted_items_print, compare=operator.lt):
    arr_sorted = merge_sort(arr, compare=operator.lt)
    if num_sorted_items_print > 0:
        print(f'\t{list(arr_sorted[:num_sorted_items_print])}', end='')
    return arr_sorted