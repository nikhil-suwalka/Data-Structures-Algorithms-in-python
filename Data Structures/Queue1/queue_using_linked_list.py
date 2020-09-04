class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


first = None
last = None


def insertAtEnd(num):
    global first, last
    if first is None:
        first = Node(num)
        last = first
    else:
        last.next = Node(num)
        last = last.next


def removeFromStart():
    global first
    temp = None
    if first is not None:
        temp = first.data
        first = first.next
    else:
        print("List not found")
    return temp


def peak():
    if last is not None:
        return last.data
    print("List is empty")
    return None


def display():
    if first is None:
        print("List is empty")
    else:
        temp = first
        while temp is not None:
            print(temp.data, end="-->")
            temp = temp.next
    print()


while True:
    n = int(input(
        "Enter choice: 1. Enqueue\t2. Dequeue\t3. Display\t4. Peak\t5. Exit\n"))
    if n == 1:
        insertAtEnd(int(input("Enter a number to push")))
    elif n == 2:
        print(removeFromStart())

    elif n == 3:
        display()

    elif n == 4:
        print(peak())

    else:
        print("Bye...")
        break
