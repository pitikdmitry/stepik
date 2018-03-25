from random import randint

p = 10123407
x = 53


def check_strings(text: str, pattern: str):
    if len(text) != len(pattern):
        return -1
    for i in range(0, len(text)):
        if text[i] != pattern[i]:
            return -1

    return 0


def get_hash(text: str):
    hash = 0
    for i in range(0, len(text)):
        hash += (ord(text[i]) * (x ** i))
    return hash


def get_second_hash(previous_hash: int, previous_str: str, current_str: str):
    previous_str_last_symbol_hash = (ord(previous_str[len(previous_str) - 1]) * (x ** (len(previous_str) - 1)))
    new_str_first_symbol_hash = (ord(current_str[0]) * (x ** 0))
    return new_str_first_symbol_hash + ((previous_hash - previous_str_last_symbol_hash) * x)


def rabin_karp_alg(pattern: str, text: str) -> None:
    if len(text) < len(pattern) or len(pattern) < 1:
        return

    P = len(pattern)
    last_hash = get_hash(text[len(text) - P:])
    pattern_hash = get_hash(pattern)
    hash_arr = [last_hash]

    for i in range(len(text) - P - 1, -1, -1):
        first_index = i
        last_index = i + P
        new_hash = get_second_hash(hash_arr[len(hash_arr) - 1], text[first_index + 1:last_index + 1], text[first_index:last_index])
        hash_arr.append(new_hash)

    for i in range(len(hash_arr) - 1, -1, -1):
        if hash_arr[i] == pattern_hash:
            if check_strings(text[len(text) - P - i:len(text) - i], pattern) == 0:
                print(len(text) - P - i, end=" ")


pattern = input()
text = input()
rabin_karp_alg(pattern, text)
