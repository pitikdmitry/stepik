
class HashTable:

    def __init__(self, m):
        self._size = m
        self._arr = []
        for i in range(0, self._size):
            self._arr.append([])

    def _get_hash(self, text: str) -> int:
        summ = 0
        p = 1000000007
        for i in range(0, len(text)):
            arg = (ord(text[i]) * 263 ** i)
            summ += arg

        return summ % p % self._size

    def find(self, text: str) -> int:
        hash = self._get_hash(text)
        chain = self._arr[hash]
        for i in range(0, len(chain)):
            if chain[i] == text:
                return 0
        return 1

    def delete(self, text: str) -> None:
        if not self.find(text):
            hash = self._get_hash(text)
            chain = self._arr[hash]
            chain.remove(text)

    def add(self, text: str) -> None:
        if self.find(text):
            hash = self._get_hash(text)
            chain = self._arr[hash]
            chain.append(text)

    def check(self, i: int) -> None:
        chain = self._arr[i]
        if len(chain) == 0:
            print("")
        else:
            for i in range(len(chain) - 1, -1, -1):
                print(chain[i], end=" ")
            print("")

m = int(input())
hashtable = HashTable(m)
n = int(input())
for i in range(0, n):
    operation, value = input().split()
    if operation == "add":
        hashtable.add(value)
    elif operation == "del":
        hashtable.delete(value)
    elif operation == "find":
        res = hashtable.find(value)
        if res == 0:
            print("yes")
        else:
            print("no")
    elif operation == "check":
        hashtable.check(int(value))
    else:
        pass