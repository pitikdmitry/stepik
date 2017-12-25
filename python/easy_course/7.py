n = int(input())
coords = [0, 0]


def move(coords: list, movement: list) -> None:
    if movement[0] == "север":
        coords[1] += movement[1]
    elif movement[0] == "юг":
        coords[1] -= movement[1]
    elif movement[0] == "запад":
        coords[0] -= movement[1]
    elif movement[0] == "восток":
        coords[0] += movement[1]


for i in range(0, n):
    movement = input().split()
    movement[1] = int(movement[1])
    move(coords, movement)

print(str(coords[0]) + " " + str(coords[1]))
