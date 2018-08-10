
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(arr)

for i in range(len(arr)):
    arr[arr.index(min(arr[i:]))], arr[i] = arr[i], min(arr[i:])

print(arr)


