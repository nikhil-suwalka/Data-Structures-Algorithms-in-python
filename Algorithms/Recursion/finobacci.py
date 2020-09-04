# Time complexity: O(N)
def fibo_iterative(n):
    f, s = 0, 1
    if n == 0:
        return 0
    for index in range(1, n + 1):
        t = f + s
        f = s
        s = t
    return f


# Time complexity: O(2^N)
def fibo_recursive(n):
    if n < 2:
        return n
    else:
        return fibo_recursive(n - 2) + fibo_recursive(n - 1)


print(fibo_iterative(35))
print(fibo_recursive(35))
