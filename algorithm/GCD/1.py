"""По данным двум числам 1≤a,b≤2⋅1091≤a,b≤2⋅109 найдите их наибольший общий делитель."""


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    elif b >= a:
        return gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
