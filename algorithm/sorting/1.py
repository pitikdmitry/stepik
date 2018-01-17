"""Первая строка содержит число 1≤n≤1051≤n≤105, вторая — массив A[1…n]A[1…n], содержащий натуральные числа, не превосходящие 109109.
 Необходимо посчитать число пар индексов 1≤i<j≤n1≤i<j≤n, для которых A[i]>A[j]A[i]>A[j]. (Такая пара элементов называется инверсией массива.
  Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в упорядоченном по
  неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)"""


counter = 0


def merge(arr1: [], arr2: []):
    first_pointer = 0
    second_pointer = 0
    result_arr = []
    global counter

    while first_pointer < len(arr1) and second_pointer < len(arr2):
        if arr1[first_pointer] <= arr2[second_pointer]:
            result_arr.append(arr1[first_pointer])
            first_pointer += 1
        else:
            counter += len(arr1) - first_pointer
            result_arr.append(arr2[second_pointer])
            second_pointer += 1

    if first_pointer == len(arr1):
        for i in range(second_pointer, len(arr2)):
            result_arr.append(arr2[i])
    elif second_pointer == len(arr2):
        for j in range(first_pointer, len(arr1)):
            result_arr.append(arr1[j])
    return result_arr


def merge_sort(arr: [], l: int, r: int):
    if l < r:
        m = int((l + r) / 2)
        return merge(merge_sort(arr, l, m), merge_sort(arr, m + 1, r))
    else:
        return arr[l:r+1]


n = int(input())
arr = input().split()

for i in range(0, len(arr)):
    arr[i] = int(arr[i])

result_arr = merge_sort(arr, 0, len(arr) - 1)
print(counter)
# print(result_arr)
