def get_hash(text: str) -> int:
    m = 5
    summ = 0
    p = 1000000007
    for i in range(0, len(text)):
        arg = (ord(text[i]) * 263 ** i)
        summ += arg

    return summ % p % m


print(get_hash("world"))


text = "dshvgavs"
print(text[0:1])