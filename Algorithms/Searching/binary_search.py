# Time complexity: O(log(N)) assuming is list is sorted

def binarySearch(arr, toSearch):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if arr[mid] == toSearch:
            return True
        if toSearch > arr[mid]:
            low = mid + 1
        elif toSearch < arr[mid]:
            high = mid - 1

    return False


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
