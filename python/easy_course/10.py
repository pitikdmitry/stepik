import requests
file_name = "dataset_3378_3.txt"


def read_file(file_name: str) -> str:
    s1 = "https://stepic.org/media/attachments/course67/3.6.3/" + file_name
    r = requests.get(s1.strip())
    text = r.text.split()
    print(r.text)
    if text[0] != "We":
        read_file(r.text)
    else:
        return r.text


with open(file_name, 'r') as inf:
    s1 = inf.readline()
    r = requests.get(s1.strip())


read_file(r.text)
