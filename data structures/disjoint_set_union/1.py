class DisjointSetUnion:

    def __init__(self):
        self._parents = []
        self._ranks = []
        self._max_rank = 0

    def add(self, parent, table_size):
        self._parents.append(parent)
        self._ranks.append(table_size)
        if table_size > self._max_rank:
            self._max_rank = table_size

    def find(self, i):
        if i != self._parents[i]:
            self._parents[i] = self.find(self._parents[i])
        return self._parents[i]

    def union(self, dest, source) -> int:
        dest_root = self.find(dest)
        source_root = self.find(source)

        if dest_root == source_root:
            return self._max_rank

        self._ranks[dest_root] = self._ranks[source_root] + self._ranks[dest_root]
        self._ranks[source_root] = 0
        self._parents[source_root] = self._parents[dest_root]
        if self._ranks[dest_root] > self._max_rank:
            self._max_rank = self._ranks[dest_root]

        return self._max_rank


n, m = map(int, input().split())
dsu = DisjointSetUnion()
table_sizes = list(map(int, input().split()))


for i in range(0, len(table_sizes)):
    dsu.add(i, table_sizes[i])

for i in range(0, m):
    destination, source = map(int, input().split()) # tables to union
    print(dsu.union(destination - 1, source - 1))
