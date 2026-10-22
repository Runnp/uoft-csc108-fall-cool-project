def rotate(L5: list) -> list:
    L6 = []
    for column in range(len(L5[0])):
        row = []
        for index in range(len(L5) - 1, -1, -1):
            row.append(L5[index][column])
        L6.append(row)
    return L6

L5 = [
    [0, 1, 0],
    [20, 0, 5],
    [0, 10, 0]
]

result = rotate(L5)

print(*result, sep="\n")