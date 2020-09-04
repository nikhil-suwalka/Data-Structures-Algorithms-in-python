def linearSearch(arr, toSearch):
    for i in arr:
        if i == toSearch:
            return True
    return False


print(linearSearch([1, 6, 7, 8, 4, 2, 3, 5, 9, 100], 100))
