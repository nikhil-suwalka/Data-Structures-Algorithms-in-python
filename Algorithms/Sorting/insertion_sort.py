numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
    return arr


def insertion_sort2(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            j -= 1

        del arr[i]
        arr.insert(j, temp)
    return arr


print(insertion_sort(numbers))
print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

print(insertion_sort2(numbers))
print(insertion_sort2([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

print(insertion_sort2([2, 4, 6, 8, 3]))
