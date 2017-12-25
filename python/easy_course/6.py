d = int(input())

words = set()
unknown_words = set()
for i in range(0, d):
    words.add(input().lower())

l = int(input())
for j in range(0, l):
    text = input().split()
    for word in text:
        word = word.lower()
        if word not in words:
            unknown_words.add(word)

for word in unknown_words:
    print(word)
