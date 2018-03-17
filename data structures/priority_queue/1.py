class MinHeap:

    def __init__(self, n):
        self._size = 0
        self._max_size = n
        self._arr = []
        self._swap_counter = 0
        self._swapped_elements = []

    def swap(self, i, j):
        self._swapped_elements.append((i, j))
        self._swap_counter += 1

        tmp = self._arr[i]
        self._arr[i] = self._arr[j]
        self._arr[j] = tmp

    def parent(self, i: int):
        return (i - 1) // 2

    def left_child(self, i: int):
        return 2 * i + 1

    def right_child(self, i: int):
        return 2 * i + 2

    def sift_up(self, i):
        while i > 0 and self._arr[self.parent(i)] > self._arr[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i):
        max_index = i
        left_child = self.left_child(i)
        if left_child < self._size and self._arr[left_child] < self._arr[max_index]:
            max_index = left_child

        right_child = self.right_child(i)
        if right_child < self._size and self._arr[right_child] < self._arr[max_index]:
            max_index = right_child

        if i != max_index:
            self.swap(i, max_index)
            self.sift_down(max_index)

    def insert(self, p):
        if self._size == self._max_size:
            return

        self._size += 1
        self._arr.append(p)
        self.sift_up(self._size - 1)

    def insert_arr(self, arr: []):
        for i in range(0, len(arr)):
            self._arr.append(arr[i])
            self._size += 1
        self.build_heap()

    def build_heap(self):
        for i in range(self._size - 1, -1, -1):
            self.sift_down(i)

    def print_result(self):
        print(self._swap_counter)
        for i in range(0, len(self._swapped_elements)):
            print("{} {}".format(self._swapped_elements[i][0], self._swapped_elements[i][1]))


n = int(input())
# n = 5
heap = MinHeap(n)
arr = list(map(int, input().split()))
# arr = [5, 4, 3, 2, 1]

heap.insert_arr(arr)
heap.print_result()
