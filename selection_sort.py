def selection_sort(arr, num_sorted_items_print):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]
    if num_sorted_items_print > 0:
        print(f'\t{list(arr[:num_sorted_items_print])}', end='')
    return arr