calculations = 0


# Time complexity: O(2^N)
def fibo(n):
    global calculations
    calculations += 1
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


cache = {}

memcalculations = 0


# Time complexity: O(N)
def memoizeFibo(n):
    global memcalculations

    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            memcalculations += 1
            cache[n] = memoizeFibo(n - 1) + memoizeFibo(n - 2)
            return cache[n]


print(fibo(20), "Calculations:", calculations)

print(memoizeFibo(20), "Calculations:", memcalculations)
