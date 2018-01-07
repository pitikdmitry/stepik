"""Первая строка содержит количество предметов 1≤n≤1031≤n≤103 и вместимость рюкзака 0≤W≤2⋅1060≤W≤2⋅106.
Каждая из следующих nn строк задаёт стоимость 0≤ci≤2⋅1060≤ci≤2⋅106 и объём 0<wi≤2⋅1060<wi≤2⋅106 предмета
(nn, WW, cici, wiwi — целые числа). Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
 с точностью не менее трёх знаков после запятой."""


def comparator(x):
    return x[0] / x[1]


def max_price(items: list, W: int) -> float:
    items.sort(key=comparator, reverse=True)
    sum_weight = 0
    sum_money = 0
    iterator = iter(items)

    while sum_weight < W:
        try:
            item = next(iterator)
        except StopIteration as e:
            break

        if sum_weight + item[1] <= W:
            sum_weight += item[1]
            sum_money += item[0]
        else:
            koef = (W - sum_weight) / item[1]
            sum_weight += koef * item[1]
            sum_money += koef * item[0]
    return sum_money


n, W = map(int, input().split())
items = []

for i in range(n):
    c, w = map(int, input().split())
    items.append((c, w))

print(max_price(items, W))
