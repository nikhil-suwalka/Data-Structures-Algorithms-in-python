def mergeSortedArrays(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if (arr1[i] < arr2[j]):
            result.append(arr1[i])
            i += 1
        elif (arr1[i] > arr2[j]):
            result.append(arr2[j])
            j += 1
        else:
            result.extend([arr1[i], arr1[i]])
            i += 1
            j += 1
    if i < len(arr1):
        for k in range(i, len(arr1)):
            result.append(arr1[k])
    elif j < len(arr2):
        for k in range(j, len(arr2)):
            result.append(arr2[k])
    return result


print(mergeSortedArrays([1, 2, 6, 8, 9], [1, 2, 5, 6]))
print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]))
