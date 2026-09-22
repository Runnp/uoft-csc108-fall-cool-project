
def assignments_contribution(a1: float, a2: float, a3: float) -> int:
    '''NOTE: The type annotations are missing! Please add them.
    Given raw marks a1, a2 and a3 for the three course assignments,
    calculate the contribution to the final course grade.
    Assume each assignment is marked out of 50.
    The assignments are worth 5%, 12.5%, and 5%, respectively, so the
    return value of this function has a max of 22.5.
    >>> assignments_contribution(30.0, 32.0, 20.0)
    13
    '''
    return int((a1 / 50 * 5) + (a2 / 50 * 12.5) + (a3 / 50 * 5))
# print(assignments_contribution(30.0, 32.0, 20.0))

def prep_review_practice_contribution(prep_review: float, practice: float) -> int:
    '''Given raw marks for prep and review (Sunday and Friday PCRS assignments)
    and practice (clickers, PCRS practice, or labs), calculate the contribution
    to the final course grade.
    NOTE: Prep and Review is marked out of 27, and practice is marked out of 8.
    The former has a contribution of 7.5%, and the latter has a contribution of
    10%,
    so the return value of this function has a max of 17.5.
    >>> prep_review_practice_contribution(18.0, 8.0)
    15
    '''
    return int((prep_review / 27 * 7.5) + (practice / 8 * 10))

def term_work_mark(assignments: float, prep_review: float, practice: float, midterm: float) -> float:
    '''Given the contribution of:
    assignments (out of 22.5)
    prepare and review (out of 7.5)
    practice (out of 10)
    and midterm (as a percentage),
    return the term mark grade.
    NOTE: the midterm is worth 30%, so the returned mark represents a mark out of
    70.
    >>> term_work_mark(16.0, 8.0, 5.0, 80.0)
    53.0
    '''
    return (assignments + prep_review + practice + (midterm / 100 * 30))
# print(term_work_mark(16.0, 8.0, 5.0, 80.0))