global linelist
global count
count = 0


def openfile(file):
    lines = []
    for line in file:
        lines.append(line)
    return lines


def search(i, j):
    global count
    leftdiag = False
    rightdiag = False
    tr = linelist[i - 1][j + 1]
    tl = linelist[i - 1][j - 1]
    br = linelist[i + 1][j + 1]
    bl = linelist[i + 1][j - 1]
    if (tl == "M" and br == "S") or (tl == "S" and br == "M"):
        leftdiag = True
    if (tr == "M" and bl == "S") or (tr == "S" and bl == "M"):
        rightdiag = True

    if rightdiag and leftdiag:
        count += 1


with open("input.txt", "r") as f:
    linelist = openfile(f)

for i in range(1, 139):
    for j in range(1, 139):
        if (linelist[i][j]) == "A":
            search(i, j)

print(f"answer 1: {count}")
