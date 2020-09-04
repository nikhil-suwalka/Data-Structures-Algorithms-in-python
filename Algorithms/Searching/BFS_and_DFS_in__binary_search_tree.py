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
                    temp = temp.left
                    temp2 = temp.right
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


def BFS():
    currentNode = root
    list = []
    queue = [currentNode]
    while len(queue) > 0:
        currentNode = queue[0]
        print(currentNode.data)
        del queue[0]
        list.append(currentNode.data)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    return list


def BFS_recursive(queue, list1):
    if len(queue) == 0:
        return list1
    currentNode = queue[0]
    list1.append(currentNode.data)
    del queue[0]
    if currentNode.left:
        queue.append(currentNode.left)
    if currentNode.right:
        queue.append(currentNode.right)
    return BFS_recursive(queue, list1)


def DFSTraverseInOrder(node, list1):
    if node.left:
        DFSTraverseInOrder(node.left, list1)
    list1.append(node.data)
    if node.right:
        DFSTraverseInOrder(node.right, list1)
    return list1


def DFSTraversePreOrder(node, list1):
    list1.append(node.data)
    if node.left:
        DFSTraversePreOrder(node.left, list1)
    if node.right:
        DFSTraversePreOrder(node.right, list1)
    return list1


def DFSTraversePostOrder(node, list1):
    if node.left:
        DFSTraversePostOrder(node.left, list1)
    if node.right:
        DFSTraversePostOrder(node.right, list1)
    list1.append(node.data)

    return list1


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

remove(9)
#          4
#        /   \
#      1       9
#     / \     / \
#    0   3   7   10
#       /   /
#      2   6


print("--._.--")

# BFS: pros: finding Shortest path is easy; cons: requires more memory
# DFS: pros: less memory, can be used to find if a path exists; cons: can get slow if tree/graph is deep

# BFS: 4,1,9,0,3,7,10,2,6
# DFS: 4,1,0,3,2,9,7,6,10
# DFS: 1. Inorder: 0,1,2,3,4,6,7,9,10
#      2. Preorder: 4,1,0,3,2,9,7,6,10
#      3. Postorder:0,2,3,1,6,7,10,9,4

print("BFS:\n\n")
print(BFS())
print(BFS_recursive([root], []))

# print("DFS\n\n")
# DFS()
print("DFS Inorder:")
print(DFSTraverseInOrder(root, []))
print("DFS preorder:")
print(DFSTraversePreOrder(root, []))
print("DFS postorder:")
print(DFSTraversePostOrder(root, []))
