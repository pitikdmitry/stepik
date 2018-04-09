from bytes_string.bytes_string import BytesString


def fill_letters(text: str, table_of_keys: {}, current_index: int) -> int:
    for c in text:
        if c == "#":
            break
        elif c not in table_of_keys:
            table_of_keys[c] = bin(current_index)
            current_index += 1

    return current_index


def fill_asccii(table_of_keys: {}, current_bit: int) -> int:
    with open("ascii.txt", 'r') as f:
        for line in f:
            for c in line:
                if c not in table_of_keys:
                    table_of_keys[c] = current_bit
                    current_bit += 1

    return current_bit


def encode_text(text: str, array_of_keys: {}, current_bit: int):
    coded_str = ""
    current_text = ""
    iterator = iter(text)
    c = next(iterator)

    while True:
        if c == " " or c == "," or c == "?" or c == "!" or c == "." or c == "#":
            if current_text not in array_of_keys:
                array_of_keys[current_text] = current_bit
            coded_str += array_of_keys[current_text]
            if c != "#":
                coded_str += array_of_keys[c]   # добавляем в строку код пробела
                current_text = ""
                c = next(iterator)
            else:
                break

        elif current_text + c in array_of_keys:
            current_text += c
            c = next(iterator)
            continue

        else:
            coded_str += array_of_keys[current_text]
            print(array_of_keys[current_text], end=" ")
            current_text += c
            array_of_keys[current_text] = bin(current_bit)
            current_bit += 1
            current_text = ""

    return coded_str


def find_key_by_value(symbol_code: str, array_of_keys: {}):
    for key, value in array_of_keys.items():
        if int(value, 2) == int(symbol_code, 2):
            return key

    return None


def decode_text(coded_str: str, array_of_keys: {}):
    decoded_str = ""
    coded_str = BytesString(coded_str)
    iterator = iter(coded_str)
    c_bit = next(iterator)

    try:
        while True:
            c = find_key_by_value(c_bit, array_of_keys)
            if c is not None:
                decoded_str += c
                c_bit = next(iterator)
            else:
                print("ERROR")
    except StopIteration:
        pass

    return decoded_str


def run_programm(text: str):
    table_of_keys = {}
    text += "#"
    current_bit = 0
    current_bit = fill_letters(text, table_of_keys, current_bit)
    coded_str = encode_text(text, table_of_keys, current_bit)
    print(coded_str)

    decoded_str = decode_text(coded_str, table_of_keys)
    print(decoded_str)
    return coded_str, decoded_str


if __name__ == "__main__":
    table_of_keys = {}
    text = input()
    text += "#"
    current_bit = 0
    current_bit = fill_letters(text, table_of_keys, current_bit)
    coded_str = encode_text(text, table_of_keys, current_bit)
    decode_text(coded_str, table_of_keys)
