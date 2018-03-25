from random import randint


def get_hash(text: str, x: int, p: int):
    hash = 0
    for i in range(0, len(text)):
        hash += (ord(text[i]) * (x ** i)) % p
    return hash

def get_second_hash(first_hash: int, x_max: int, x: int, old_symbol: str, new_symbol: str):
    hash = (first_hash - ord(old_symbol) * x_max) * x + ord(new_symbol)


def rabin_karp_alg(pattern: str, text: str) -> None:
    if len(text) < len(pattern) or len(pattern) < 1:
        return

    p = 1000007
    x = randint(0, p)
    P = len(pattern)
    x_max = (x ** (P - 1)) % p
    last_hash = get_hash(text[P + 1:], x, p)
    pattern_hash = get_hash(pattern, x, p)

    hash_arr = [last_hash]
    for i in range(len(text) - P - 1, -1, -1):
        first_index = i
        last_index = i + P
        current_text = text[first_index: last_index]
        hash_arr.append(get_hash(text[first_index:last_index], x, p))

    for i in range(len(hash_arr) - 1, -1, -1):
        if hash_arr[i] == pattern_hash:
            print(len(text) - P - i, end=" ")


pattern = input()
text = input()
rabin_karp_alg(pattern, text)
