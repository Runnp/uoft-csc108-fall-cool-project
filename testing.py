
def exam_required(term_work: float, desired_grade: int) -> float:
    '''Given a term work mark of term_work representing 70% of the points in the
    grading scheme, calculate and return the percentage required on the exam for
    the final mark to be desired_grade.
    >>> exam_required(46.0, 82)
    120.0
    '''
    return ((desired_grade - term_work) / 30 * 100)
print(exam_required (46.0, 82))