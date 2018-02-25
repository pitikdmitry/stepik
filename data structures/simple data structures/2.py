# Максимум в скользящем окне


class MaxStack:
    def __init__(self):
        self._arr = []
        self._current_max = 0

    def push(self, key):
        if key > self._current_max:
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


def fill_second_stack(stack_in: MaxStack, stack_out: MaxStack):
    while not stack_in.empty():
        val = stack_in.pop()
        stack_out.push(val[0])


def print_max_in_window(arr: [], m: int) -> None:
    if m > len(arr):
        return

    stack_in = MaxStack()
    stack_out = MaxStack()
    array_counter = 0

    for i in range(0, m):
        stack_in.push(arr[i])
        array_counter += 1

    while True:
        if array_counter <= len(arr):
            if stack_out.empty():
                fill_second_stack(stack_in, stack_out)

            second_max = stack_out.pop()[1]
            if not stack_in.empty():
                first_max = stack_in.top()[1]
                maximum = max(first_max, second_max)
                print(maximum)
            else:
                print(second_max)

            if array_counter < len(arr):
                stack_in.push(arr[array_counter])
            array_counter += 1
        else:
            return


n = int(input())
input_arr = list(map(int, input().split()))
m = int(input())
print_max_in_window(input_arr, m)

