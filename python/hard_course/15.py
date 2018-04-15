import requests


def parse_res(res, answers: []):
    text = res.text
    text_arr = text.split("\n")
    for par in text_arr:
        par_arr = par.split(":")
        if par_arr[0].find("found") != -1:
            if par_arr[1].find("true") != -1:
                answers.append(True)
            else:
                answers.append(False)


url = "http://numbersapi.com/"
url_part2 = "/math"
numbers = []
params = {
    "json": "true"
}
answers = []

with open("file.txt", 'r') as f:
    for line in f:
        numbers.append(int(line))

for number in numbers:
    current_url = url + str(number) + url_part2
    res = requests.get(current_url, params=params)
    parse_res(res, answers)

with open("file.txt", "w") as f:
    for answer in answers:
        if answer:
            f.write("Interesting\n")
        else:
            f.write("Boring\n")
