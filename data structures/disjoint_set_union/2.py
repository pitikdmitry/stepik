class DisjointSetUnion:

    def __init__(self, n):
        self._parents = []
        self._ranks = []
        for i in range(0, n):
            self._add(i, 1)

    def _add(self, parent, table_size):
        self._parents.append(parent)
        self._ranks.append(table_size)

    def find(self, i):  # переподвешиваем
        if i != self._parents[i]:
            self._parents[i] = self.find(self._parents[i])
        return self._parents[i]

    def union(self, val1, val2):
        val1_root = self.find(val1)
        val2_root = self.find(val2)

        if val1_root == val2_root:
            return

        if self._ranks[val1_root] > self._ranks[val2_root]:
            self._parents[val2_root] = self._parents[val1_root]
        else:
            if self._ranks[val1_root] == self._ranks[val2_root]:
                self._ranks[val2_root] += 1
            self._parents[val1_root] = self._parents[val2]

        return

    def check_pair(self, val1, val2) -> int:
        val1_root = self.find(val1)
        val2_root = self.find(val2)

        if val1_root == val2_root and val1_root != -1:
            return -1
        else:
            return 0


n, e, d = map(int, input().split())
dsu = DisjointSetUnion(n)

for _ in range(0, e):
    i_eq, j_eq = map(int, input().split())
    dsu.union(i_eq - 1, j_eq - 1)

bad_flag = False
for _ in range(0, d):
    i_n_eq, j_n_eq = map(int, input().split())
    res = dsu.check_pair(i_n_eq - 1, j_n_eq - 1)
    if res == -1:
        bad_flag = True
        break

if bad_flag:
    print("0")
else:
    print("1")
