class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = None


def insert(data):
    global root
    if not root:
        root = Node(data)
    else:
        temp = root
        while True:
            if data < temp.data:
                if not temp.left:
                    temp.left = Node(data)
                    return
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = Node(data)
                    return
                else:
                    temp = temp.right


insert(10)
insert(5)
insert(15)
insert(1)
insert(6)
insert(13)
insert(20)

#        10
#     5      15
#   1  6   13   20
#
#

print()
print()


def inorder(current: Node):
    if current.left:
        inorder(current.left)
    print(current.data)
    if current.right:
         inorder(current.right)

def preorder(current:Node):
    print(current.data)
    if current.left:
        preorder(current.left)
    if current.right:
         preorder(current.right)

def postorder(current:Node):

    if current.left:
        postorder(current.left)
    if current.right:
         postorder(current.right)
    print(current.data)

print("InOrder:")
inorder(root)
print("\nPreOrder:")
preorder(root)
print("\nPostOrder:")
postorder(root)