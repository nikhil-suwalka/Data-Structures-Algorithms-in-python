arr1 = []
arr2 = []


def push(data):
    arr1.append(data)


def pop():
    global arr1
    if (len(arr1) > 0):
        a = arr1[len(arr1) - 1]
        del arr1[len(arr1) - 1]
        return a
    print("Underflow")
    return None


def display():
    if len(arr1) == 0:
        print("Stack is empty")
    else:
        for i in range(len(arr1) - 1, -1, -1):
            print(f"{arr1[i]} --> ")


def peak():
    if len(arr1) > 0:
        return arr1[len(arr1) - 1]
    else:
        print("Stack is empty")
        return None


def push2(data):
    arr2.append(data)


def pop2():
    global arr2
    if (len(arr2) > 0):
        a = arr2[len(arr2) - 1]
        del arr2[len(arr2) - 1]
        return a
    print("Underflow")
    return None



while True:
    n = int(input(
        "Enter choice: 1. Push\t2. Pop\t3. Display\t4. Peak\t5. Exit\n"))
    if n == 1:
        if len(arr1) == 0:
            push(int(input("Enter a number to push")))
        else:
            while len(arr1) > 0:
                push2(pop())
            push(int(input("Enter a number to push")))
            while len(arr2) > 0:
                push(pop2())

    elif n == 2:
        print(pop())

    elif n == 3:
        display()

    elif n == 4:
        print(peak())

    else:
        print("Bye...")
        break
