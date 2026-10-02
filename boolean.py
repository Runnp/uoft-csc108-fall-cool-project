def marathon_time (half_time: int, hilly: bool) -> int:
    estimation = 0
    if hilly:
        estimation = half_time * 2 + 30
    else:
        estimation = half_time * 2 + 15
    return estimation
print(marathon_time (20, True))


def total_ticket_price(n_reg_tic: int, n_stu_tic: int, holiday: bool) -> int:
    reg_ticket = 4.5
    student_ticket = 2.5
    total = reg_ticket * n_reg_tic + student_ticket * n_stu_tic
    if holiday:
        if (n_reg_tic + n_stu_tic) >= 6:
            total = total * 0.95
    else:
        if (n_reg_tic + n_stu_tic) >= 10:
            total = total * 0.9
    return round(total, 2)
# print(total_ticket_price(8, 2, True))
#(8 * 4.50 + 2 * 2.5) * 0.95 = 38,95

def australian_timezone(time: float, toronto_day: bool, melbourne_day: bool) -> float:
    if toronto_day and melbourne_day:
        time = time + 15
    elif toronto_day and not melbourne_day:
        time = time + 14
    else:
        time = time + 16
    return time % 24
# print(australian_timezone(17, True, False))
# print(australian_timezone(6, False, True))
# print(australian_timezone(10, True, True))