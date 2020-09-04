def add80(num):
    print("Long time")
    return num + 80


print(add80(5))
print(add80(5))
print(add80(5))

cache = {}


def memoizeAdd80(num):
    if num in cache:
        return cache[num]
    else:
        print("Long time")
        cache[num] = num + 80
        return cache[num]


print("\n\n")
print(memoizeAdd80(5))

# uses cache(memoize)
print(memoizeAdd80(5))

# uses cache(memoize)
print(memoizeAdd80(5))

print(memoizeAdd80(6))

# uses cache(memoize)
print(memoizeAdd80(6))
