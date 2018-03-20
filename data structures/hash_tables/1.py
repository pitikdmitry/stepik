class HashTable:

    def __init__(self):
        self._size = 100
        self._arr = []
        self._real_size = 0
        for i in range(0, self._size):
            self._arr.append(-1)

    def _get_hash(self, key, j) -> int:
        return (int(key) + j) % self._size

    def delete(self, key: int) -> None:
        counter = 0
        hash = self._get_hash(key, counter)

        while self._arr[hash] != -1:
            val = self._arr[hash]
            if val != "deleted" and val[0] == key:
                self._arr[hash] = "deleted"
                self._real_size -= 1
                return
            counter += 1
            hash = self._get_hash(key, counter)

    def find(self, key: int) -> str:
        counter = 0
        hash = self._get_hash(key, counter)

        while self._arr[hash] != -1:
            val = self._arr[hash]
            if val != "deleted" and val[0] == key:
                return self._arr[hash][1]
            counter += 1
            hash = self._get_hash(key, counter)

        return "not found"

    def _check_memory(self):
        if self._real_size / self._size > 0.75:

            new_arr = []
            self._size *= 2
            for i in range(0, self._size):
                new_arr.append(-1)

            for i in range(0, len(self._arr)):
                if self._arr[i] == -1:
                    continue

                if self._arr[i] == "deleted":
                    continue

                key = self._arr[i][0]
                counter = 0
                hash = self._get_hash(key, counter)
                while new_arr[hash] != -1:
                    counter += 1
                    hash = self._get_hash(key, counter)

                new_arr[hash] = self._arr[i]

            self._arr = new_arr

    def add(self, key: int, value: str) -> None:
        counter = 0
        hash = self._get_hash(key, counter)

        while self._arr[hash] != -1:
            val = self._arr[hash]
            if val == "deleted":
                break

            if val[0] == key:
                self._arr[hash] = (key, value)
                return
            counter += 1
            hash = self._get_hash(key, counter)

        self._arr[hash] = (key, value)
        self._real_size += 1
        self._check_memory()


def parse_query(query_arr: [], hash_table: HashTable) -> None:
    if query_arr[0] == "add":
        hash_table.add(int(query_arr[1]), query_arr[2])
    elif query_arr[0] == "del":
        hash_table.delete(int(query_arr[1]))
    elif query_arr[0] == "find":
        res = hash_table.find(int(query_arr[1]))
        if res == "not found":
            print("not found")
        else:
            print(str(res))
    else:
        pass


n = int(input())
hash_table = HashTable()
for i in range(0, n):
    query_arr = input().split()
    parse_query(query_arr, hash_table)
