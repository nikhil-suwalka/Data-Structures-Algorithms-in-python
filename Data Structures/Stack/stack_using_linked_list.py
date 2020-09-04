class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


bottom = None
top = None
length = 0


def insertAtEnd(num):
    global bottom, top, length
    if bottom is None:
        bottom = Node(num)
        top = bottom
    else:
        top.next = Node(num)
        top = top.next
    length += 1


def removeFromEnd():
    global top, length, bottom
    temp2 = None
    if bottom is not None:

        if bottom.next is None:
            temp2 = top.data
            bottom = None
        else:
            temp = bottom
            while temp.next is not top:
                temp = temp.next
            temp.next = None
            temp2 = top.data
            del top
            top = temp
        length -= 1
    else:
        print("List is empty")
        return None
    return temp2


def peak():
    if top is not None:
        return top.data
    print("List is empty")
    return None


def display():
    if bottom is None:
        print("List is empty")
    else:
        temp = bottom
        while temp is not None:
            print(temp.data, end="\n----\n")
            temp = temp.next


while True:
    n = int(input(
        "Enter choice: 1. Push\t2. Pop\t3. Display\t4. Peak\t5. Exit\n"))
    if n == 1:
        insertAtEnd(int(input("Enter a number to push")))
    elif n == 2:
        print(removeFromEnd())

    elif n == 3:
        display()

    elif n == 4:
        print(peak())

    else:
        print("Bye...")
        break
