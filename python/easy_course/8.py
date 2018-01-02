def add_to_dict(class_number: int, height: int, people: dict) -> None:
    if class_number in people:
        people[class_number].append(height)
    else:
        people[class_number] = [height]


def do_calculation(people: dict) -> dict:
    result = dict()
    for key in people:
        summ = 0
        for i in people[key]:
            summ += i

        for j in range(1, key):
            if j not in result:
                result[j] = "-"

        result[key] = summ / len(people[key])

    return result


people = dict()
with open("dataset_3380_5.txt", 'r') as inf:
    for line in inf:
        l1 = line.split()
        add_to_dict(int(l1[0]), int(l1[2]), people)


result = do_calculation(people)
for key, val in result.items():
    print(str(key) + " " + str(val))

