# stack


class Stack:

    def __init__(self):
        self._arr = []

    def push(self, key: str) -> None:
        self._arr.append(key)

    def empty(self) -> bool:
        return len(self._arr) <= 0

    def pop(self) -> str:
        if not self.empty():
            self._arr.pop()
        else:
            return None

    def top(self) -> str:
        if not self.empty():
            last_index = len(self._arr) - 1
            return self._arr[last_index]

    def size(self) -> int:
        return len(self._arr)

    def last_open(self) -> int:
        if self.empty():
            return 0
        previous = None
        for i in range(len(self._arr) - 1, -1, -1):
            if self._arr[i] in (')', ']', '}'):
                previous = self._arr[i]
                continue
            if previous is not None:
                if (previous == ')' and self._arr[i] == '(') or (previous == ']' and self._arr[i] == '[') or (previous == '}' and self._arr[i] == '{'):
                    self._arr.pop(i)

                    self._arr.pop(i)    # тут не правильно
                    return self.last_open()
                elif self._arr[i] in ('(', '[', '{'):
                    return i + 1
                else:
                    self._arr.pop(i)
            else:
                if self._arr[i] in ('(', '[', '{'):
                    return i + 1

        return 0


def is_balanced(str) -> int:
    stack = Stack()
    stack_for_indexing = Stack()

    for char in str:

        if char not in ('}', ')', ']'): # октрывающие и мусор
            stack.push(char)
        else:   # закрывающие скобки
            if stack.empty():
                return stack_for_indexing.size() + 1

            top = stack.top()
            while top not in ('[', '{', '(', ')', ']', '}') and stack.size() > 0:
                top = stack.pop()
                top = stack.top()

            if (top == '[' and char == ']') or (top == '{' and char == '}') or(top == '(' and char == ')'):
                stack.pop()
            else:
                return stack_for_indexing.size() + 1

        stack_for_indexing.push(char)

    if stack.empty():
        return 0
    else:
        return stack_for_indexing.last_open()


input_str = input()
if len(input_str) == 0:
    print(0)
else:
    result_index = is_balanced(input_str)
    if result_index != 0:
        print(str(result_index))
    else:
        print("Success")


def check(stri):
    res = is_balanced(stri)
    print(res)
    return res


assert check("([](){([])})") == 0
assert check("()[]}") == 5
assert check("{{[()]]") == 7
assert check("{{{[][][]") == 3
assert check("{*{{}") == 3
assert check("[[*") == 2
assert check("{*}") == 0
assert check("{{") == 2
assert check("{}") == 0
assert check("") == 0
assert check("}") == 1
assert check("*{}") == 0
assert check("{{{**[][][]") == 3
assert check("([]){()") == 5

assert check("([](){([])})") == 0
assert check("()[]}") == 5
assert check("{{[()]]") ==7
assert check("{{{[][][]") ==3
assert check("{{") == 2
assert check("{}") == 0
assert check("") == 0
assert check("}") == 1
assert check("s{}") == 0
assert check("{{{ss[][][]") == 3
assert check("(((((((((())))") == 3
