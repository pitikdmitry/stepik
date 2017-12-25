def check_counter(counter: int, n: int) -> bool:
    if counter > n * n:
        return True
    # return False


def spiral_array(arr: [], n: int):
    high_f = 0
    high_e = n

    right_f = 1
    right_e = n

    down_f = n - 2
    down_e = -1

    left_f = n - 2
    left_e = 0

    counter = 1
    cycle_asc = 0
    cycle_desc = n - 1

    while True:
        for i in range(high_f, high_e):
            arr[cycle_asc][i] = counter
            counter += 1
            if check_counter(counter, n):
                return

        for j in range(right_f, right_e):
            arr[j][cycle_desc] = counter
            counter += 1
            if check_counter(counter, n):
                return

        for k in range(down_f, down_e, -1):
            arr[cycle_desc][k] = counter
            counter += 1
            if check_counter(counter, n):
                return

        for m in range(left_f, left_e, -1):
            arr[m][cycle_asc] = counter
            counter += 1
            if check_counter(counter, n):
                return

        high_f += 1
        high_e -= 1

        right_f += 1
        right_e -= 1

        down_f -= 1
        down_e += 1

        left_f -= 1
        left_e += 1

        cycle_desc -= 1
        cycle_asc += 1


n = int(input())
arr = []
for i in range(0, n):
    arr.append([])
    for j in range(0, n):
        arr[i].append(0)

spiral_array(arr, n)

for i in range(0, n):
    for j in range(0, n):
        print(arr[i][j], end=' ')
    print("")

