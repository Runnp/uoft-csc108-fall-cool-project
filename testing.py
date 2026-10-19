def find_letter_n_times(s: str, letter: str, n: int) -> str:
    """Return the smallest substring of s starting from index 0 that contains
        n occurrences of letter.

        Precondition: letter occurs at least n times in s

        >>> find_letter_n_times('Computer Science', 'e', 2)
        'Computer Scie'
        """
    if n == 0:
        return ''
    count = 0
    for i in range(len(s)):
        if s[i] == letter:
             count += 1
             if count == n:
                return s[:i + 1]


def count_collatz_steps(n: int) -> int:
        """Return the number of steps it takes to reach 1, by repeating the two
        steps of the Collatz conjecture beginning from n.

        >>> count_collatz_steps(6)
        8
        """
        i = 0

        while n != 1:
                if n % 2 == 0:
                        n = n // 2
        else:
                n = n * 3 + 1
        i += 1

        return i
