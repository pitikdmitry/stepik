s = input()
t = input()


def count_sub_str(s: str, t: str, index_start: int, index_end: int, counter: int) -> int:
    while True:
        i = s.find(t, index_start, index_end)

        if i != -1:
            counter += 1
            return count_sub_str(s, t, i + 1, len(s), counter)
        else:
            return counter


print(count_sub_str(s, t, 0, len(s), 0))
