global linelist
global count
count = 0


def openfile(file):
    lines = []
    for line in file:
        lines.append(line)
    return lines


def rightsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i][j + k]
    if string == "XMAS":
        print("right")
        count += 1


def leftsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i][j - k]
    if string == "XMAS":
        print("left")
        count += 1


def topsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i - k][j]
    if string == "XMAS":
        print("top")
        count += 1


def bottomsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i + k][j]
    if string == "XMAS":
        print("bottom")
        count += 1


def topleftsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i - k][j - k]
    if string == "XMAS":
        print("topleft")
        count += 1


def toprightsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i - k][j + k]
    if string == "XMAS":
        print("topright")
        count += 1


def bottomleftsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i + k][j - k]
    if string == "XMAS":
        print("bottomleft")
        count += 1


def bottomrightsearch(i, j):
    global count
    string = ""
    for k in range(4):
        string += linelist[i + k][j + k]
    if string == "XMAS":
        print("bottomright")
        count += 1


def search(i, j):
    if j < 137:
        rightsearch(i, j)
    if j > 2:
        leftsearch(i, j)
    if i > 2:
        topsearch(i, j)
    if i < 137:
        bottomsearch(i, j)
    if (i > 2) and (j > 2):
        topleftsearch(i, j)
    if (i > 2) and (j < 137):
        toprightsearch(i, j)
    if (i < 137) and (j > 2):
        bottomleftsearch(i, j)
    if (i < 137) and (j < 137):
        bottomrightsearch(i, j)


with open("input.txt", "r") as f:
    linelist = openfile(f)

for i in range(140):
    for j in range(140):
        if linelist[i][j] == "X":
            search(i, j)

print(f"answer 1: {count}")
