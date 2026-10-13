a = [0, 1, 2]
b = a
b[2] = 100

print(a == [0, 1, 2] and b == [0, 1, 100])
print(a == [0, 1, 2] and b == [0, 100, 2])
print(a == [0, 1, 100] and b == [0, 1, 100])
print(id(a) == id(b))