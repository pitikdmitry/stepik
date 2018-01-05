def primes():
    i = 2

    while True:
        prime = True

        for j in range(2, i):
            if i % j == 0 and i != j and j != 1:
                prime = False

        if prime:
            print(i, end=" ")
            yield i

        i += 1


gen = primes()
while True:
    x = next(gen)
    if x > 31:
        break
