"""Первая строка входа содержит число операций 1≤n≤1051≤n≤105.
Каждая из последующих nn строк задают операцию одного из следующих двух типов:

InsertInsert xx, где 0≤x≤1090≤x≤109 — целое число;
ExtractMaxExtractMax.
Первая операция добавляет число xx в очередь с приоритетами, вторая — извлекает максимальное число и выводит его."""


class MaxHeap:

    def __init__(self):
        self._arr = []

    def swap(self, a, b):
        temp = self._arr[a]
        self._arr[a] = self._arr[b]
        self._arr[b] = temp

    def sift_up(self, i):
        while i > 0:
            parent = int((i - 1) / 2)
            if self._arr[parent] < self._arr[i]:
                self.swap(parent, i)
            else:
                break
            i = parent

    def sift_down(self, i):
            child_1 = 2 * i + 1
            child_2 = 2 * i + 2

            biggest = i
            if child_1 < len(self._arr) and self._arr[child_1] > self._arr[biggest]:
                biggest = child_1
            if child_2 < len(self._arr) and self._arr[child_2] > self._arr[biggest]:
                biggest = child_2

            if biggest != i:
                self.swap(i, biggest)
                self.sift_down(biggest)

    def extract_max(self):
        result = self._arr[0]
        self.swap(0, len(self._arr) - 1)
        self._arr.pop()
        self.sift_down(0)
        return result

    def insert(self, value):
        self._arr.append(value)
        self.sift_up(len(self._arr) - 1)
        # print(self._arr)


n = int(input())
heap = MaxHeap()
for i in range(n):
    items = input().split()
    oper = items[0]
    if oper == "Insert":
        value = int(items[1])
        heap.insert(value)
    elif oper == "ExtractMax":
        max_value = heap.extract_max()
        print(max_value)
