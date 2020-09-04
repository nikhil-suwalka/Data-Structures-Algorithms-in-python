class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = None
tail = None
length = 0


def insertAtEnd(num):
    global head, tail, length
    if head is None:
        head = Node(num)
        tail = head
    else:
        tail.next = Node(num)
        tail = tail.next
    length += 1


def insertAtStart(num):
    global head, tail, length
    if head is None:
        head = Node(num)
        tail = head
    else:
        temp = Node(num, head)
        head = temp
    length += 1


def traverseToIndex(index):
    temp = head
    i = 0
    while i < index:
        i += 1
        temp = temp.next
    return temp


def insert(index, value):
    global length
    if length == index:
        insertAtEnd(value)
    elif length < index:
        print("Index not found")
    elif index == 0:
        insertAtStart(value)
    else:

        temp = traverseToIndex(index - 1)
        temp.next = Node(value, temp.next)
        length += 1


def removeFromStart():
    global head, length

    if head is not None:
        head = head.next
        length -= 1
    else:
        print("List not found")


def removeFromEnd():
    global tail, length, head
    if head is not None:

        if head.next is None:
            head = None
        else:
            temp = head
            while temp.next is not tail:
                temp = temp.next
            temp.next = None
            del tail
            tail = temp
        length -= 1

    else:
        print("List not found")


def removeByIndex(index):
    global length
    if index == 0:
        removeFromStart()
    elif index == length - 1:
        removeFromEnd()
    elif index >= length:
        print("Index not found")
    else:
        temp = traverseToIndex(index - 1)
        temp.next = temp.next.next
        length -= 1


def display():
    if head is None:
        print("List is empty")
    else:
        temp = head
        while temp is not None:
            print(temp.data, end="-->")
            temp = temp.next
    print()


def search(toSearch):
    if head is None:
        print("List is empty")
    else:
        temp = head
        while temp is not None:
            if temp.data == toSearch:
                print("Found")
                return 0
            temp = temp.next
        print("Not found")


def sortList():
    if head is None:
        print("List is empty")
    elif length == 1:
        print("Already sorted")
    else:
        temp = head
        while temp.next is not None:
            temp2 = temp.next
            mini = temp
            while temp2 is not None:
                if temp2.data < mini.data:
                    mini = temp2
                temp2 = temp2.next
            temp.data, mini.data = mini.data, temp.data
            temp = temp.next


def reverseList():
    global head, tail
    f, s = None, None
    t = head

    while t is not None:
        f = s
        s = t
        t = t.next
        s.next = f
    head, tail = tail, head


while True:
    n = int(input(
        "Enter choice: 1. Insert at end\t2. Insert at start\t3. Display\t4. Get length of the list\t5. Insert at "
        "index\t6. Remove from start\t7. Remove from end\t8. Remove by index\t9. Search by data\t10. Sort the "
        "list\t11. Reverse the list\t12. Exit\n"))
    if n == 1:
        insertAtEnd(int(input("Enter a number to insert at the end")))
    elif n == 2:
        insertAtStart(int(input("Enter a number to insert at the beginning")))
    elif n == 3:
        display()
    elif n == 4:
        print(length)
    elif n == 5:
        insert(int(input("Enter index")), int(input("Enter value")))
    elif n == 6:
        removeFromStart()
    elif n == 7:
        removeFromEnd()
    elif n == 8:
        removeByIndex(int(input("Enter index")))
    elif n == 9:
        search(int(input("Enter data to search")))
    elif n == 10:
        sortList()
    elif n == 11:
        reverseList()
    else:
        print("Bye...")
        break
