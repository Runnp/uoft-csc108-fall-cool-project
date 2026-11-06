# def michael_function(points):
#     result = 0
#     for i, value in enumerate(points):
#         if i % 2 == 0:
#             result += value
#     return result
#
# print(michael_function([3, 10, 11, 12, 9]))

# def second_largest(numbers):
#     largest = second = numbers[0]
#     for num in numbers[1:]:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second:
#             second = num
#     return second
#
# print(second_largest([1,2,3,4,5,6,7,8,9]))

# with open("practical.txt") as source:
#     values = source.readline().strip().split(";")
#     print(values)


# file = open("practical.txt")
# A = file.readline()
# # print(A)
# B = file.readline()
# # print(B)
# C = file.readline()
# # print(C)
# D = file.readline()
# print(D)

# file = open("practical.txt")
# for line in file:
#     if int(line) >= 30:
#         print(line, end="")

# file = open("companies.txt")
#
# for line in file:
#     data = line.split("|")
#
#     if data[2] == "125":
#         print(data[0])

# file = open("practical.txt")
# for line in file:
#     data = line.split("|")
#
#     if len(data) >= 3 and data[2].strip() == "125":
#         print(data[0])
#         # Since the first line has three elements, but its last value is "125\n" and not "125", the comparison fails.
        # In this case, .strip() fixes the issue, while len(data) >= 3 prevents the cases where lines might have less
        # than three elements

# with open(input_filename, "r") as input_file:
#     with open(output_filename, "w") as output_file:
#         for line in input_file:
#             data = line.strip().split("|")
#             revenue = int(data[2])
#             if revenue >= minimum:
#                 output_file.write(data[0] + "," + data[2] + "\n")

x = 0
outer = 0
inner = 0
while outer < 3:
    outer = outer + 1
    while inner < 2:
        inner = inner + 1
        x = x + 1
    x = x + 1
print(x)