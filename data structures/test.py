from random import randint

t0 = 12
t1 = 423
p = 146
x = randint(0, p)

val1 = (t0 * (x ** 1) % p) + (t1 * (x ** 2) % p)
val2 = ((t0 * (x ** 0) % p) + (t1 * (x ** 1) % p)) * x % p
val3 = (t0 * (x ** 0) % p) * x % p + (t1 * (x ** 1) % p) * x % p
print(val1)
print(val2)
print(val3)


print()
x1 = 124423
x2 = 7326423
print((x1 + x2) % p)
print(x1 % p + x2 % p)
