"""Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа kk и ll через пробел — количество различных букв,
 встречающихся в строке, и размер получившейся закодированной строки, соответственно. В следующих kk строках записаны
 коды букв в формате "letter: code". Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке.
  В качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке хотя бы один раз.
   Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет
    минимальный возможный размер.
В первой строке выходного файла выведите строку ss. Она должна состоять из строчных букв латинского алфавита.
 Гарантируется, что длина правильного ответа не превосходит 104104 символов.
"""


class Node:

    def __init__(self, name: str, priority: int, left_child: object, right_child: object):
        self._name = name
        self._priority = priority
        self._left_child = left_child
        self._right_child = right_child
        self._extracted = False

    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def priority(self) -> int:
        return self._priority

    def left_child(self):
        return self._left_child

    def set_left_child(self, node: object):
        self._left_child = node

    def right_child(self):
        return self._right_child

    def set_right_child(self, node: object):
        self._right_child = node

    def extracted(self) -> bool:
        return self._extracted

    def set_extracted(self, val):
        self._extracted = val


def print_tree(node: Node):
    if node is None:
        return

    print(node.name())
    print_tree(node.left_child())
    print_tree(node.right_child())


def build_binary_tree(letters: dict) -> Node:
    head = Node("head", 1, None, None)

    for letter, code in letters.items():
        current_node = head
        last_bit = code[len(code) - 1]
        code = code[:-1]

        for bit in code:
            new_node = Node("K", 1, None, None)
            if bit == "0" and current_node.left_child() is None:
                current_node.set_left_child(new_node)
            elif bit == "1" and current_node.right_child() is None:
                current_node.set_right_child(new_node)

            if bit == "0":
                current_node = current_node.left_child()
            elif bit == "1":
                current_node = current_node.right_child()

        new_node = Node(letter, 1, None, None)
        if last_bit == "0" and current_node.left_child() is None:
            current_node.set_left_child(new_node)
        elif last_bit == "0" and current_node.left_child() is not None:
            current_node.left_child().set_name(letter)
        elif last_bit == "1" and current_node.right_child() is None:
            current_node.set_right_child(new_node)
        elif last_bit == "1" and current_node.right_child() is not None:
            current_node.right_child().set_name(letter)

    # print_tree(head)
    return head


def decode_text(head: Node, coded_text: str) -> str:
    decoded_str = ""
    current_node = head
    iterator = iter(coded_text)
    try:
        char = next(iterator)
        while True:
            if char == "0" and current_node.left_child() is not None:
                current_node = current_node.left_child()
                char = next(iterator)
            elif char == "0" and current_node.left_child() is None:
                decoded_str += current_node.name()
                current_node = head
            elif char == "1" and current_node.right_child() is not None:
                current_node = current_node.right_child()
                char = next(iterator)
            elif char == "1" and current_node.right_child() is None:
                decoded_str += current_node.name()
                current_node = head
    except StopIteration:
        if char == "0" and current_node.left_child() is None:
            decoded_str += current_node.name()
        elif char == "1" and current_node.right_child() is None:
            decoded_str += current_node.name()

    return decoded_str


letters_amount, code_length = map(int, input().split())
letters = dict()

for i in range(0, letters_amount):
    letter, code = map(str, input().split(": "))
    letters[letter] = code

coded_text = input()

head_node = build_binary_tree(letters)
decoded_str = decode_text(head_node, coded_text)
print(decoded_str)













