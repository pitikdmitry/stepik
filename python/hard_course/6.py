def func(n):
    if n % 2 == 0:
        return True
    return False


filter_obj = filter(func, [1, 2, 3, 4])
print(next(filter_obj))


filter_obj_2 = filter(lambda n: n % 2 == 0, [1, 2, 3, 4])
print(next(filter_obj_2))
