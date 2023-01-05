import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
         
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0 
        j = 0 
        k = 0 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def randomArray(size):
    arr = []
    k = size
    for i in range(k):
        x = random.randint(0, 1000000)
        arr.append(x)
    return arr

class TreeNode():
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

def height(self):
    if self is None:
        return 0 
    leftAns = height(self.left)
    rightAns = height(self.right)
 
    return max(leftAns, rightAns) + 1
            
def randomTree(arr, size):
    tree = TreeNode(arr[0])
    for i in range(1, size):
        tree.insert(arr[i])
    return tree

def randomTreap(arr, size):
    treap = Treap()
    for i in range(size):
        key = random.randint(1, size)
        value = arr[i]
        treap.insert(key, value)
    return treap

def getLeafCount(self):
    if self is None:
        return 0 
    if(self.left is None and self.right is None):
        return 1 
    else:
        return getLeafCount(self.left) + getLeafCount(self.right)

class Node:
    def __init__(self, key, value, priority, left=None, right=None):
        self.key = key
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
    
class Treap:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
    
    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value, random.random())
        if key < node.key:
            node.left = self._insert(node.left, key, value)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key, value)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        return node
    
    def _rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        return left
    
    def _rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

def get_height(self):
    if not self:
        return 0
    return 1 + max(get_height(self.left), get_height(self.right))

size = 200
arr = randomArray(size)
print("TreeNode No sorted:")
tree = randomTree(arr, size)
print("Height of the binary tree is: " + str(height(tree)-1))
print("Quantity of leaves: " + str(getLeafCount(tree)))

print("TreapNode No sorted:")
tree = randomTreap(arr, size)
print("Height of the binary tree is: " + str(get_height(tree.root)-1))
print("Quantity of leaves: " + str(getLeafCount(tree.root)))

merge_sort(arr)

print("TreeNode Sorted:")
tree = randomTree(arr, size)
print("Height of the binary tree is: " + str(height(tree)-1))
print("Quantity of leaves: " + str(getLeafCount(tree)))

print("TreapNode Sorted:")
tree = randomTreap(arr, size)
print("Height of the binary tree is: " + str(get_height(tree.root)-1))
print("Quantity of leaves: " + str(getLeafCount(tree.root)))
