import doctest
def scholarship(cgpa: float, year_of_study: int, major: str) -> float:
    """Requirements for being eligible for a scholarship are having CGPA above 3.7 and studying in 2 or 3 year of study
    >>> scholarship(3.8, 2, 'CS')
    True
    >>> scholarship(3.5, 3, 'Computer Science')
    False """
    if (major == "CS" or major == "cs" or major == "Computer Science"):
        if (cgpa > 3.7):
            if (year_of_study == 2 or year_of_study == 3):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(scholarship(3.8, 1, "Biology"))
print(scholarship(4.0, 2, "Chemistry"))
doctest.testmod()

