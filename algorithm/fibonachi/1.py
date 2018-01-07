"""Дано целое число 1≤n≤401≤n≤40, необходимо вычислить nn-е число Фибоначчи
(напомним, что F0=0F0=0, F1=1F1=1 и Fn=Fn−1+Fn−2Fn=Fn−1+Fn−2 при n≥2n≥2)."""


def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    before_brevious = 0
    previous = 1
    current = 0

    for i in range(2, n + 1):
        current = before_brevious + previous
        before_brevious = previous
        previous = current

    return current


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()