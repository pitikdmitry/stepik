str_example = input()
str_code = input()
str_to_format = input()
str_to_unformat = input()


def format_str(str_to_format: str, cipher: dict) -> str:
    new_str = ""
    for j in range(0, len(str_to_format)):
        new_str += cipher.get(str_to_format[j])

    return new_str


def unformat_str(str_to_unformat: str, uncipher: dict) -> str:
    new_str = ""
    for j in range(0, len(str_to_unformat)):
        new_str += uncipher.get(str_to_unformat[j])

    return new_str


cipher = {}
uncipher = {}

for i in range(0, len(str_example)):
    cipher[str_example[i]] = str_code[i]
    uncipher[str_code[i]] = str_example[i]


print(format_str(str_to_format, cipher))
print(unformat_str(str_to_unformat, uncipher))
