dictionary = ["month", "year", "day", "half_of_day", "decade", "century"]
string_one = "year"
string_two = "half_of_day"
def later(string_one, string_two):
    if string_one in dictionary and string_two in dictionary:
        one = dictionary.index(string_one)
        two = dictionary.index(string_two)
        return string_one if one > two else string_two
    return -1
print(later(string_one, string_two))