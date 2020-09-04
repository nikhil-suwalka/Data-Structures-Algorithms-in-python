numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(arr):
    for i in range(len(arr) - 1):
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr


print(selection_sort(numbers))
print(selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
