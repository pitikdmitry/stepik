from bytes_string.bytes_string import BytesString


def fill_first_letters(text: str, table_of_keys: {}, current_index: int) -> int:
    for c in text:
        if c == "#":
            break
        elif c not in table_of_keys:
            table_of_keys[c] = bin(current_index)
            current_index += 1

    return current_index


def fill_asccii(table_of_keys: {}, current_index: int) -> int:
    with open("ascii.txt", 'r') as f:
        for line in f:
            for c in line:
                if c not in table_of_keys:
                    table_of_keys[c] = current_index
                    current_index += 1

    return current_index


def encode_text(text: str, array_of_keys: {}, current_index: int):
    coded_str = ""
    current_text = ""
    iterator = iter(text)
    c = next(iterator)

    while True:
        if c == "#":
            if current_text != "":
                coded_str += str(array_of_keys[current_text])
                coded_str += "#"
                print(array_of_keys[current_text], end=" ")
            break
        elif c == " " or c == "," or c == "?" or c == "!" or c == ".":
            if current_text not in array_of_keys:
                array_of_keys[current_text] = current_index
            coded_str += str(array_of_keys[current_text])
            coded_str += str(array_of_keys[c])   # добавляем в строку код пробела
            current_text = ""
            c = next(iterator)
        elif current_text + c in array_of_keys:
            current_text += c
            c = next(iterator)
            continue
        else:
            coded_str += str(array_of_keys[current_text])
            print(array_of_keys[current_text], end=" ")
            current_text += c
            array_of_keys[current_text] = bin(current_index)
            current_index += 1
            current_text = ""

    return coded_str


def find_key_by_value(symbol_code: str, array_of_keys: {}):
    for key, value in array_of_keys.items():
        if int(value, 2) == int(symbol_code):
            return key

    return None


def decode_text(coded_str: str, array_of_keys: {}):
    decoded_str = ""
    coded_str = BytesString(coded_str)
    iterator = iter(coded_str)
    c = next(iterator)
    current_text = ""

    try:
        while True:
            if find_key_by_value(current_text + c, array_of_keys) is not None:
                current_text += c
                c = next(iterator)
            else:
                if find_key_by_value(current_text, array_of_keys)
                decoded_str +=
                current_text = ""
    except StopIteration:
        pass

    print("")
    print(decoded_str)
    return decoded_str


def run_programm(text: str):
    table_of_keys = {}
    text += "#"
    current_index = 0
    current_index = fill_first_letters(text, table_of_keys, current_index)
    coded_str = encode_text(text, table_of_keys, current_index)
    return coded_str, decode_text(coded_str, table_of_keys)


if __name__ == "__main__":
    table_of_keys = {}
    text = input()
    text += "#"
    current_index = 0
    current_index = fill_first_letters(text, table_of_keys, current_index)
    coded_str = encode_text(text, table_of_keys, current_index)
    decode_text(coded_str, table_of_keys)
