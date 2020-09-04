numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubbleSort(numbers))
print(bubbleSort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
