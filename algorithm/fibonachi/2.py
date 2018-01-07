"""Дано число 1≤n≤1071≤n≤107, необходимо найти последнюю цифру nn-го числа Фибоначчи.
Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
 В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
 если 0≤a,b≤90≤a,b≤9 — последние цифры чисел FiFi и Fi+1Fi+1 соответственно, то (a+b)mod10(a+b)mod10 — последняя цифра числа Fi+2Fi+2.
"""


def fib_digit(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    before_previous = 0
    previous = 1
    current = 0

    for i in range(2, n + 1):
        current = (previous + before_previous) % 10
        before_previous = previous
        previous = current

    return current



def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()