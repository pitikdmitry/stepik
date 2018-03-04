# Высота дерева


import sys


def height_rec(parent: int, arr: []):
    max_height = 1
    for val in arr[parent]:
        current_height = height_rec(val, arr) + 1
        max_height = max(max_height, current_height)
    return max_height


sys.setrecursionlimit(20000)
n = int(input())
if n != 0:
    elements = list(map(int, input().split()))
    parent_index = -1
    arr = [[] for i in range(n)]
    for i in range(0, len(elements)):
        if elements[i] == -1:
            parent_index = i
            continue
        arr[elements[i]].append(i)

    print(height_rec(parent_index, arr))
else:
    print(str(0))
