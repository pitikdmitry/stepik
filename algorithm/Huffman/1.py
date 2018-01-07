"""По данной непустой строке ss длины не более 104104,
состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв kk, встречающихся в строке, и размер получившейся закодированной строки.
В следующих kk строках запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку."""


class Node:

    def __init__(self, name: str, priority: int, left_child: object, right_child: object):
        self._name = name
        self._priority = priority
        self._left_child = left_child
        self._right_child = right_child
        self._extracted = False

    def name(self) -> str:
        return self._name

    def priority(self) -> int:
        return self._priority

    def left_child(self) -> object:
        return self._left_child

    def right_child(self) -> object:
        return self._right_child

    def extracted(self) -> bool:
        return self._extracted

    def set_extracted(self, val):
        self._extracted = val


class PriorityQueue:

    def __init__(self):
        self._arr = []
        self._top = None

    def length(self):
        return len(self._arr)

    def top(self):
        return self._top

    def extract_min(self) -> Node:
        if len(self._arr) == 0:
            raise BaseException

        min_priority_node = None
        for node in self._arr:
            if node.extracted() is not True:
                min_priority_node = node
                node.set_extracted(True)
                break
        for node in self._arr:
            if min_priority_node is not None and node.extracted() is False \
                    and node.priority() < min_priority_node.priority():
                min_priority_node.set_extracted(False)
                node.set_extracted(True)
                min_priority_node = node

        return min_priority_node

    def insert(self, node: Node) -> None:
        self._top = node
        self._arr.append(node)


def pre_order_tree(node: Node, value: str, result_str: str, result_code: dict):
    if node is None:
        return
    if node.name() == value:
        result_code[node.name()] = result_str
        return

    result_str += "0"
    pre_order_tree(node.left_child(), value, result_str, result_code)

    result_str = result_str[:-1]
    result_str += "1"
    pre_order_tree(node.right_child(), value, result_str, result_code)
    result_str = result_str[:-1]


def get_full_code(text: str, result_code: dict) -> str:
    coded_text = ""
    for char in text:
        coded_text += result_code[char]

    return coded_text


def get_pairs(text: str) -> {}:
    pairs = {}
    for char in text:
        if char not in pairs:
            pairs[char] = 1
        else:
            pairs[char] += 1

    return pairs


def huffman(pairs: dict, result_code: dict):
    priority_queue = PriorityQueue()
    for key, value in pairs.items():
        node = Node(key, value, None, None)
        priority_queue.insert(node)

    while True:
        min_node_1 = priority_queue.extract_min()
        if min_node_1 is None:
            break
        min_node_2 = priority_queue.extract_min()
        if min_node_2 is None:
            break
        new_node = Node(min_node_1.name() + min_node_2.name(), min_node_1.priority() + min_node_2.priority(), min_node_1,
                        min_node_2)
        priority_queue.insert(new_node)

    result_str = ""

    if len(pairs) == 1:
        result_code[priority_queue.top().name()] = "0"
    else:
        for key, value in pairs.items():
            pre_order_tree(priority_queue.top(), key, result_str, result_code)


s = input()
pairs = get_pairs(s)
result_code = dict()
huffman(pairs, result_code)
coded_text = get_full_code(s, result_code)

print(len(pairs), len(coded_text))
for key, value in result_code.items():
    print(key + ": " + str(value))

print(coded_text)

