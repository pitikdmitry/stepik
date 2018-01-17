"""Дано целое число 1≤n≤1031≤n≤103 и массив A[1…n]A[1…n] натуральных чисел, не превосходящих 2⋅1092⋅109.
 Выведите максимальное 1≤k≤n1≤k≤n, для которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n1≤i1<i2<…<ik≤n длины kk,
 в которой каждый элемент делится на предыдущий (формально: для  всех 1≤j<k1≤j<k, A[ij]|A[ij+1]A[ij]|A[ij+1])."""


def LISBottomUp(arr: []) -> int:
    d = []
    max_subsequence = 1

    for i in range(0, len(arr)):
        d.append(1)
        for j in range(0, i - 1):
            if arr[j] < arr[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                if d[i] > max_subsequence:
                    max_subsequence = d[i]

    return max_subsequence


def max_subsequence_division(arr: []) -> int:
    d = []
    if len(arr) < 1:
        return 0

    max_subsequence = 1

    for i in range(0, len(arr)):
        d.append(1)
        for j in range(0, i):
            if arr[i] % arr[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                if d[i] > max_subsequence:
                    max_subsequence = d[i]

    return max_subsequence


n = int(input())
arr = [int(x) for x in input().split()]

# print(LISBottomUp(arr))
print(max_subsequence_division(arr))
