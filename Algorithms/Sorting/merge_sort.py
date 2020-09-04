# Time complexity: O(N log(n))

import math

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = math.ceil(len(arr) / 2)
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))


def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])
    return result


print(mergeSort(numbers))
print(mergeSort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
