def foo(x: int) -> int:
    """If x is negative use abs() function to make it positive.
    Then, calculate the square of x using another function named 'square'.
    This function should be defined in the global scope and not be nested.
    """

    def is_negative(x: int) -> bool:
        if x < 0:
            return abs(x)

    return square(x)


def square(x: int) -> int:
    x = x ** 2
    return x