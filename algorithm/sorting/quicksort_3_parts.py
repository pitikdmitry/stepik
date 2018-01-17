from random import randint


def swap(arr: [], first: int, second: int):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def partition(arr: [], l: int, r: int):
    pivot = randint(l, r)
    swap(arr, pivot, l)
    x = arr[l]
    j = l
    me = l
    for i in range(l + 1, r + 1):
        if arr[i] < x:
            me += 1
            j += 1
            swap(arr, j, me)
            if i != me:
                swap(arr, i, j)
        elif arr[i] == x:
            me += 1
            swap(arr, me, i)

    swap(arr, l, j)
    return j, me


def quick_sort(arr: [], l: int, r: int):
    if l >= r:
        return

    m, me = partition(arr, l, r)
    quick_sort(arr, l, m - 1)
    quick_sort(arr, me + 1, r)


arr = []
for i in range(0, 10):
    arr.append(randint(0, 100))

print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
