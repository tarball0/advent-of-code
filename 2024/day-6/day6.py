def movevertical(map, direction):
    global pos
    global guardgone
    global count
    while True:
        if ((pos[0] == 0) or (pos[0] >= len(map)-1)):
            guardgone = True
            break
        if (map[pos[0]-direction][pos[1]] == '#'):
            break
        pos[0] -= direction
        if map[pos[0]][pos[1]] != "X":
            map[pos[0]][pos[1]] = "X"
            count += 1


def movehorizontal(map, direction):
    global pos
    global guardgone
    global count
    while True:
        if ((pos[1] == 0) or (pos[1] >= len(map)-1)):
            guardgone = True
            break
        if (map[pos[0]][pos[1]+direction] == '#'):
            break
        pos[1] += direction
        if map[pos[0]][pos[1]] != "X":
            map[pos[0]][pos[1]] = "X"
            count += 1


map = []
global pos
global guardgone
global count
count = 0
guardgone = False
with open("input.txt", "r") as input:
    for line in input:
        map.append(list(line))

for line in map:
    for char in line:
        if char == '^':
            pos = [map.index(line), line.index(char)]

map[pos[0]][pos[1]] = "X"

while True:
    movevertical(map, 1)
    if guardgone:
        break
    movehorizontal(map, 1)
    if guardgone:
        break
    movevertical(map, -1)
    if guardgone:
        break
    movehorizontal(map, -1)
    if guardgone:
        break

print(f"count = {count+1}")
