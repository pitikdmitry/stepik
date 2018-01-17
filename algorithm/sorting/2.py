"""В первой строке задано два целых числа 1≤n≤500001≤n≤50000 и 1≤m≤500001≤m≤50000 — количество отрезков и точек на прямой,
 соответственно. Следующие nn строк содержат по два целых числа aiai и bibi (ai≤biai≤bi) — координаты концов отрезков.
  Последняя строка содержит mm целых чисел — координаты точек. Все координаты не превышают 108108 по модулю.
   Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
    Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""

from random import randint


def compare_left(first, second):
    if first[0] < second[0]:
        return 1
    elif first[0] == second[0]:
        if first[1] < second[1]:
            return 1
        elif first[1] == second[1]:
            return 0
    return -1


def compare_right(first, second):
    if first[1] < second[1]:
        return 1
    elif first[1] == second[1]:
        if first[0] < second[0]:
            return 1
        elif first[0] == second[0]:
            return 0
    return -1


def swap(arr: [], first: int, second: int):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def partition(arr: [], l: int, r: int, compare):
    pivot = randint(l, r)
    swap(arr, pivot, l)
    x = arr[l]
    j = l
    me = l  #последний элемент равных

    for i in range(l + 1, r + 1):
        if compare(arr[i], x) == 1:
            j += 1
            me += 1
            swap(arr, j, me)
            if i != me:
                swap(arr, i, j)
        elif compare(arr[i], x) == 0:
            me += 1
            swap(arr, me, i)

    swap(arr, l, j)
    return j, me


def quick_sort(arr: [], l: int, r: int, compare):
    while l < r:
        m, me = partition(arr, l, r, compare)
        quick_sort(arr, l, m - 1, compare)
        # quick_sort(arr, me + 1, r, compare)
        l = me + 1


def binary_search_right(arr: [], k: int, f_or_s: int) -> int:
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if k < arr[m][f_or_s]:
            r = m
        else:
            l = m + 1
    return l


def binary_search_left(arr: [], k: int, f_or_s: int) -> int:
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m][f_or_s] < k:
            l = m + 1
        else:
            r = m
    return l


def find_intersects(segments_left: [], segments_right: [], dot: int):
    counter_left = binary_search_right(segments_left, dot, 0)

    counter_right = binary_search_left(segments_right, dot, 1)

    return counter_left - counter_right


n, m = map(int, input().split())
segments_left = []
segments_right = []
for i in range(0 , n):
    l, r = map(int, input().split())
    segments_left.append((l, r))
    segments_right.append((l, r))

quick_sort(segments_left, 0, len(segments_left) - 1, compare_left)
quick_sort(segments_right, 0, len(segments_right) - 1, compare_right)

dots = input().split()

for j in range(0, len(dots)):
    k = find_intersects(segments_left, segments_right, int(dots[j]))
    print(k, end=" ")
