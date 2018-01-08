"""В первой строке даны целое число 1≤n≤1051≤n≤105 и массив A[1…n]A[1…n] из nn различных натуральных чисел, н
е превышающих 109109, в порядке возрастания, во второй — целое число 1≤k≤1051≤k≤105 и kk натуральных чисел b1,…,bkb1,…,bk,
не превышающих 109109. Для каждого ii от 1 до kk необходимо вывести индекс 1≤j≤n1≤j≤n,
 для которого A[j]=biA[j]=bi, или −1−1, если такого jj нет.
"""


def binary_search(arr: [], k: int) -> int:
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = int((l + r) / 2)
        if arr[m] == k:
            return m
        elif arr[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1


arr_1 = []
map_obj = map(int, input().split())
n = next(map_obj)
for i in map_obj:
    arr_1.append(i)

arr_2 = []
map_obj = map(int, input().split())
k = next(map_obj)
for i in map_obj:
    arr_2.append(i)

for j in arr_2:
    index = binary_search(arr_1, j)
    if index != -1:
        index += 1
    print(index, end=" ")


