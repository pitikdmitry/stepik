class Node:
    def __init__(self, key, value, left, right):
        self._key = key
        self._value = value
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._size = 0
        self._root = None

    def add(self, key, value, left, right):
        node = Node(key, value, left, right)
        if self._root is None:
            self._root = node


n = int(input())
tree = BinaryTree()
for i in range(0, n):
    key, left, right = map(int, input().split())
    tree.add(key, i, left, right)
