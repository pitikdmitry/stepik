from random import randint

p = 20
x = 5


def get_hash(text: str):
    hash = 0
    p = 20
    x = 5
    for i in range(0, len(text)):
        hash += (ord(text[i]) * (x ** i)) % p
        em3 = (ord(text[i]) * (x ** i)) % p
    return hash


def get_second_hash(previous_hash: int, previous_str: str, current_str: str):
    p = 20
    x = 5
    previous_str_last_symbol_hash = (ord(previous_str[len(previous_str) - 1]) * (x ** (len(previous_str) - 1))) % p
    new_str_first_symbol_hash = (ord(current_str[0]) * (x ** 0)) % p
    hash = new_str_first_symbol_hash + (previous_hash - previous_str_last_symbol_hash) * x
    return hash


def rabin_karp_alg(pattern: str, text: str) -> None:
    if len(text) < len(pattern) or len(pattern) < 1:
        return
    p = 20
    x = 5

    P = len(pattern)
    em2 = text[len(text) - P:]
    last_hash = get_hash(text[len(text) - P:])
    pattern_hash = get_hash(pattern)
    hash_arr = [last_hash]

    for i in range(len(text) - P - 1, -1, -1):
        first_index = i
        last_index = i + P
        em = text[first_index:last_index]
        new_hash = get_second_hash(hash_arr[len(hash_arr) - 1], text[first_index + 1:last_index + 1], text[first_index:last_index])
        hash_arr.append(new_hash)

    for i in range(len(hash_arr) - 1, -1, -1):
        if hash_arr[i] == pattern_hash:
            print(len(text) - P - i, end=" ")


pattern = input()
text = input()
rabin_karp_alg(pattern, text)
