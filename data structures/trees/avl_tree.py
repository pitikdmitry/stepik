class Node:
    def __init__(self, key):
        self._key = key
        self._height = 1
        self._left = None
        self._right = None

    @property
    def key(self):
        return self._key

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node: "Node"):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node: "Node"):
        self._right = node

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val


class Tree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, key):
        self._root = Node(key)

    def in_order(self):
        self._in_order(self._root)

    def _in_order(self, node: Node):
        if node is None:
            return

        print(node.key)
        self._in_order(node.left)
        self._in_order(node.right)

    def bfs(self, node: Node):
        queue = []
        values = []

        queue.append(node)

        while len(queue) > 0:
            temp_node = queue.pop(0)
            values.append(temp_node.key)
            if temp_node.left is not None:
                queue.append(temp_node.left)
            if temp_node.right is not None:
                queue.append(temp_node.right)

        for val in values:
            print(val)

    def _fix_height(self, node: Node):
        if node is None:
            return

        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height

        node.height = max(left_height, right_height) + 1

    def _b_factor(self, node: Node) -> int:
        if node is None:
            return 0

        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height

        return right_height - left_height

    def _balance(self, node: Node):
        self._fix_height(node)

        if self._b_factor(node) == 2:
            if self._b_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        if self._b_factor(node) == -2:
            if self._b_factor(node.left) > 0:
                p.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        return node

    def _rotate_right(self, node: Node):
        a = node
        b = node.left
        a.left = b.right
        b.right = a
        self._fix_height(a)
        self._fix_height(b)
        return b

    def _rotate_left(self, node: Node):
        a = node
        b = node.right
        a.right = b.left
        b.left = a
        self._fix_height(a)
        self._fix_height(b)
        return b

    def insert(self, key):
        if self._root is not None:
            self._root = self._insert(self._root, key)
        else:
            self._root = Node(key)

    def _insert(self, node: Node, key):
        if node is None:
            return Node(key)

        if key <= node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return self._balance(node)


tree = Tree()
for i in range(0, 10):
    tree.insert(i)

# tree.in_order()
tree.bfs(tree.root)
