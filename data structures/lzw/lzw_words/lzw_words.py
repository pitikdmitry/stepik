from bytes_string.bytes_string import BytesString

letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"


def encode_text(text: str, array_of_keys: {}, current_bit: int):
    coded_str = ""
    current_text = ""

    for c in text:
        if c in letters:
            current_text += c
        else:

            if current_text != "" and current_text not in array_of_keys:
                array_of_keys[current_text] = bin(current_bit)
                coded_str += array_of_keys[current_text]
                current_bit += 1
                current_text = ""

            if c != "#":
                if c not in array_of_keys:
                    array_of_keys[c] = bin(current_bit)
                    current_bit += 1
                coded_str += array_of_keys[c]

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

    try:
        c_bit = next(iterator)
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
    coded_str = encode_text(text, table_of_keys, current_bit)
    decoded_str = decode_text(coded_str, table_of_keys)
    return coded_str, decoded_str


if __name__ == "__main__":
    table_of_keys = {}
    text = input()
    text += "#"
    current_bit = 0
    coded_str = encode_text(text, table_of_keys, current_bit)
    decode_text(coded_str, table_of_keys)
