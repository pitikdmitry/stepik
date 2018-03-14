class Queue:

    def __init__(self, buff_size: int):
        self._buff_size = buff_size
        self._arr = []

    def push(self, val):
        arrival = val[0]
        duration = val[1]
        if not self.empty():
            if arrival >= self.top():   # may be we need to check only >
                self.pop()
        self._arr.append(val)

    def pop(self) -> tuple:
        return self._arr.pop()

    def top(self) -> tuple:
        #   returns first
        if not self.empty():
            return self._arr[0]

    def empty(self) -> bool:
        if not self.empty():
            return len(self._arr) == 0


buff_size, n = map(int, input().split())
for i in range(0, n):
    arrival, duration = map(int, input().split())




