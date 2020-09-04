class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = None


def insert(data):
    global root
    if root is None:
        root = Node(data)
    else:
        temp = root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = Node(data)
                    break
                else:
                    temp = temp.right


def search(data):
    if root is None:
        print("Tree is empty")
    else:
        temp = root
        while temp is not None:
            if data == temp.data:
                return True
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False


# To delete with 2 child, find minimum in right sub tree -> copy value to target node and then delete
# duplicate from right sub tree

def remove(data):
    global root
    if root is None:
        print("Tree is empty")
    elif (root.data == data):
        if root.data == data:
            if root.left is root.right is None:
                root = None
            elif root.left is None and root.right is not None:
                root = root.right
            elif root.right is None and root.left is not None:
                root = root.left
            else:
                temp = root
                temp2 = root.right
                while temp2.left is not None:
                    temp = temp2
                    temp2 = temp.left
                root.data = temp2.data
                temp.left = None
    else:
        temp = root
        while temp is not None:
            if temp.left is not None and temp.left.data == data:
                if temp.left.left is None and temp.left.right is None:
                    temp.left = None
                elif temp.left.left is None and temp.left.right is not None:
                    temp.left = temp.left.right
                elif temp.left.left is not None and temp.left.right is None:
                    temp.left = temp.left.left
                else:
                    temp = temp.right
                    temp2 = temp
                    while temp2.left.left is not None:
                        temp2 = temp2.left
                    temp.data = temp2.left.data
                    temp2.left = None
                break
            elif temp.right is not None and temp.right.data == data:
                if temp.right.left is None and temp.right.right is None:
                    temp.right = None
                elif temp.right.left is None and temp.right.right is not None:
                    temp.right = temp.right.right
                elif temp.right.left is not None and temp.right.right is None:
                    temp.right = temp.right.left
                else:
                    temp = temp.right
                    temp2 = temp
                    while temp2.left.left is not None:
                        temp2 = temp2.left
                    temp.data = temp2.left.data
                    temp2.left = None
                break

            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right


insert(4)
insert(1)
insert(3)
insert(9)
insert(7)
insert(6)
insert(2)
insert(0)
insert(10)
print(search(7))
print(search(2))
print(search(20))
print(search(1))

#          4
#        /   \
#      1       9
#     / \     / \
#    0   3   7   10
#       /   /
#      2   6

remove(1)



print("--._.--")
