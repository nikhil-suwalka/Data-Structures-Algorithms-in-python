def reverse(string):
    if (type(string) != str):
        return "hmm that's not good"
    str2 = ""
    for i in range(len(string) - 1, -1, -1):
        str2 += string[i]
    return str2


def reverse2(string):
    if (type(string) != str):
        return "hmm that's not good"
    str2 = ""
    for i in string:
        str2 = i + str2
    return str2


def reverse3(string):
    if (type(string) != str):
        return "hmm that's not good"
    return string[::-1]


print(reverse("Nikhil"))
print(reverse2("Nikhil"))
print(reverse3("Nikhil"))

print(reverse(45))
