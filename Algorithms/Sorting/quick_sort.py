# Time complexity: O(N log(n))

# arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# arr = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
pass1 = 1
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def quick(start, end):
    global pass1
    s = start
    n = end

    pivot = start
    start += 1
    while (start <= end):
        if (numbers[pivot] >= numbers[start]):
            start += 1
        elif (numbers[pivot] < numbers[end]):
            end -= 1
        else:
            numbers[start], numbers[end] = numbers[end], numbers[start]
    numbers[end], numbers[pivot] = numbers[pivot], numbers[end]
    print("Pass: ", pass1, numbers)
    pass1 += 1
    if (end >= s + 2):
        quick(s, end - 1)
    if (end <= n - 2):
        quick(end + 1, n)


quick(0, len(numbers) - 1)
print(numbers)
