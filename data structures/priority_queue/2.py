class PriorityQueue:

    def __init__(self, n):
        self._size = 0
        self._max_size = n
        self._arr = []

    def parent(self, i: int):
        return (i - 1) // 2

    def left_child(self, i: int):
        return 2 * i + 1

    def right_child(self, i: int):
        return 2 * i + 2

    def swap(self, i, j):
        tmp = self._arr[i]
        self._arr[i] = self._arr[j]
        self._arr[j] = tmp

    def sift_up(self, i):
        while i > 0 and self._arr[self.parent(i)][1] >= self._arr[i][1]:
            if self._arr[self.parent(i)][1] == self._arr[i][1]:
                if self._arr[self.parent(i)][0] > self._arr[i][0]:
                    self.swap(self.parent(i), i)
                    i = self.parent(i)
            else:
                self.swap(self.parent(i), i)
                i = self.parent(i)

    def sift_down(self, i):
        max_index = i
        left_child = self.left_child(i)
        if left_child < self._size and self._arr[left_child][1] <= self._arr[max_index][1]:
            if self._arr[left_child][1] == self._arr[max_index][1]:
                if self._arr[left_child][0] < self._arr[max_index][0]:
                    max_index = left_child
            else:
                max_index = left_child

        right_child = self.right_child(i)
        if right_child < self._size and self._arr[right_child][1] <= self._arr[max_index][1]:
            if self._arr[right_child][1] == self._arr[max_index][1]:
                if self._arr[right_child][0] < self._arr[max_index][0]:
                    max_index = right_child
            else:
                max_index = right_child

        if i != max_index:
            self.swap(i, max_index)
            self.sift_down(max_index)

    def insert(self, val):
        if self._size == self._max_size:
            return

        self._size += 1
        self._arr.append(val)
        self.sift_up(self._size - 1)

    def add_without_rules(self, val):
        if self._size == self._max_size:
            return

        self._size += 1
        self._arr.append(val)

    def top(self):
        if not self._size == 0:
            return self._arr[0]

    def add_task(self, task_time):
        top = self.top()
        print("{} {}".format(top[0], top[1]))  # printing proc number, time when the task will start to execute
        top[1] += task_time
        self.sift_down(0)


n, m = list(map(int, input().split()))  # n - proc, m - tasks
queue = PriorityQueue(n)
for i in range(0, n):   # adding proccesors to the queue
    queue.add_without_rules([i, 0])

tasks = list(map(int, input().split()))
for i in range(0, m):
    queue.add_task(tasks[i])
