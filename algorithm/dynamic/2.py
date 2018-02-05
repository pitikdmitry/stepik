"""Вычислите расстояние редактирования двух данных непустых строк длины не более 102102,
 содержащих строчные буквы латинского алфавита."""


def diff(a: str, b: str) -> int:
    if a == b:
        return 0
    return 1


def EditDistBu(first: str, second: str) -> int:
    n = len(first) + 1
    m = len(second) + 1
    arr = [[0 for j in range(0, m)] for i in range(0, n)]

    for i in range(0, n):
        arr[i][0] = i

    for j in range(0, m):
        arr[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            c = diff(first[i - 1], second[j - 1])
            arr[i][j] = min(arr[i - 1][j] + 1, arr[i][j - 1] + 1, arr[i - 1][j - 1] + c)

    return arr[len(first)][len(second)]


first = input()
second = input()
print(EditDistBu(first, second))
