"""По данному числу 1≤n≤1091≤n≤109 найдите максимальное число kk, для которого nn можно представить
 как сумму kk различных натуральных слагаемых. Выведите в первой строке число kk, во второй — kk слагаемых."""


def find_max_digits(n) -> list:
    result_digits = []
    if n == 0:
        return result_digits
    elif n == 1:
        result_digits.append(1)
        return result_digits
    else:
        counter = 1
        while n >= counter:
            if n - counter > counter:
                n -= counter
                result_digits.append(counter)
                counter += 1
            else:
                result_digits.append(n)
                break
    return result_digits


n = int(input())
result_digits = find_max_digits(n)
print(len(result_digits))
for i in result_digits:
    print(i, end=" ")
