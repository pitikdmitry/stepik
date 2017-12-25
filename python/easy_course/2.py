word = input()

previous_char = ''
amount = 0
result_str = ''
counter = 0

for c in word:
    if previous_char == c:
        amount += 1
    elif previous_char != c:
        if amount != 0:
            result_str = result_str + previous_char
            result_str = result_str + str(amount)
        previous_char = c
        amount = 1

    counter += 1
    if len(word) == counter:
        result_str += previous_char
        result_str += str(amount)

print(result_str)