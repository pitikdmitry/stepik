class Multiplicity:
    def __init__(self, size):
        self._size = size




n, m = map(int, input().split())
# n - number of tables
# m - number of queries
multiplicities = []
table_sizes = list(map(int, input().split()))
for i in range(0, len(table_sizes)):
    multiplicity = Multiplicity(table_sizes[i])

for i in range(0, m):
    destination, source = map(int, input().split()) # tables to union