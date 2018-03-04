# Стек с максимумом


class MaxStack:
    def __init__(self):
        self._arr = []
        self._current_max = None

    def push(self, key):
        if self._current_max is None:
            self._current_max = key
        elif key > self._current_max:
            self._current_max = key

        self._arr.append((key, self._current_max))

    def empty(self) -> bool:
        return len(self._arr) <= 0

    def top(self):
        if not self.empty():
            return self._arr[len(self._arr) - 1]

    def pop(self):
        if not self.empty():
            val = self._arr.pop()
            if not self.empty():
                self._current_max = self.top()[1]
            else:
                self._current_max = 0
            return val

    def max(self):
        if self._current_max is not None:
            return self._current_max


def parse_input(input_str: str, max_stack: MaxStack):
    input_list = input_str.split()
    if input_list[0] == "push":
        max_stack.push(int(input_list[1]))
    elif input_list[0] == "pop":
        max_stack.pop()
    elif input_list[0] == "max":
        maximum = max_stack.max()
        if maximum is not None:
            print(maximum)
    else:
        return


max_stack = MaxStack()
n = int(input())
for i in range(0, n):
    input_str = input()
    parse_input(input_str, max_stack)