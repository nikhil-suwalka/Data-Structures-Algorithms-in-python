def fact(num):
    if num <= 1:
        return 1
    return num * fact(num - 1)


def fact2(num):
    return 1 if num <= 1 else num * fact(num - 1)


print(fact(5))
print(fact2(5))