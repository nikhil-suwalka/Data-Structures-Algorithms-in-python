arr1 = []


def push(data):
    arr1.append(data)


def pop():
    global arr1
    if (len(arr) > 0):
        a = arr[len(arr)-1]
        del arr[len(arr)-1]
        return a
    print("Underflow")
    return None


def display():
    if len(arr1) == 0:
        print("Stack is empty")
    else:
        for i in range(len(arr1) - 1, -1, -1):
            print(f"{arr1[i]}\n----\n")


def peak():
    if len(arr1) > 0:
        return arr1[len(arr1) - 1]
    else:
        print("Stack is empty")
        return None


while True:
    n = int(input(
        "Enter choice: 1. Push\t2. Pop\t3. Display\t4. Peak\t5. Exit\n"))
    if n == 1:
        push(int(input("Enter a number to push")))
    elif n == 2:
        print(pop())

    elif n == 3:
        display()

    elif n == 4:
        print(peak())

    else:
        print("Bye...")
        break
