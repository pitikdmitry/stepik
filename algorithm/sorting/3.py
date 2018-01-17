"""count sort"""


def count_sort(arr: list) -> list:
    b_mass = [0 for x in range(0, 11)]

    for i in arr:
        b_mass[i] += 1

    for i in range(2, len(b_mass)):
        b_mass[i] = b_mass[i] + b_mass[i - 1]

    result_arr = [0 for x in range(0, len(arr))]

    for j in range(len(arr) - 1, -1, -1):
        result_arr[b_mass[arr[j]] - 1] = arr[j]
        b_mass[arr[j]] -= 1

    return result_arr


arr = list()
n = int(input())

arr = [int(x) for x in input().split()]
result_arr = count_sort(arr)
for j in result_arr:
    print(j, end=" ")
