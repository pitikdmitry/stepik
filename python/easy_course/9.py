import requests

s1 = ""
with open('dataset_3378_2.txt', 'r') as inf:
    s1 = inf.readline()

r = requests.get(s1.strip())
n = r.text.splitlines()
print(len(n))
