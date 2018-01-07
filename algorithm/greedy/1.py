"""По данным nn отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤1001≤n≤100 отрезков.
Каждая из последующих nn строк содержит по два числа 0≤l≤r≤1090≤l≤r≤109, задающих начало и конец отрезка.
Выведите оптимальное число mm точек и сами mm точек. Если таких множеств точек несколько, выведите любое из них."""


def print_result(points: list) -> None:
    print(len(points))
    for point in points:
        print(point, end=" ")


def remove_intersects(segments: list, point: int) -> None:
    result_list = []
    for segment in segments:
        if not (segment[0] <= point <= segment[1]):
            result_list.append(segment)

    return result_list


def find_min_right_segment(segments: list) -> tuple:
    min_right = segments[0]
    for segment in segments:
        if segment[1] < min_right[1]:
            min_right = segment
    return min_right


def min_amount_of_points(segments: list):
    points = list()

    while len(segments) > 0:
        min_right = find_min_right_segment(segments)
        if min_right is not None:
            points.append(min_right[1])
            segments = remove_intersects(segments, min_right[1])
    print_result(points)


n = int(input())
segments = list()

for i in range(n):
    point = input().split()
    left = int(point[0])
    right = int(point[1])
    pair = (left, right)
    segments.append(pair)

min_amount_of_points(segments)


