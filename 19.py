def next_day(dt_tuple):
    if ((dt_tuple[2] % 4 == 0) and (dt_tuple[2] % 100 != 0)) or (dt_tuple[2] % 400 == 0):
        leap_year = True
        feb_days = 29
    else:
        leap_year = False
        feb_days = 28
    month_days = {1: 31, 2: feb_days, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if dt_tuple[1] == month_days[dt_tuple[0]]:
        if dt_tuple[0] < 12:
            return dt_tuple[0] + 1, 1, dt_tuple[2], (dt_tuple[3] + 1) % 7
        else:
            return 1, 1, dt_tuple[2] + 1, (dt_tuple[3] + 1) % 7
    else:
        return dt_tuple[0], dt_tuple[1] + 1, dt_tuple[2], (dt_tuple[3] + 1) % 7


dates = []
dt_tuple = (1, 1, 1901, 2)

while dt_tuple[2] < 2001:
    dates.append(dt_tuple)
    dt_tuple = next_day(dt_tuple)

sundays = [i for i in dates if (i[1] == 1) and (i[3] == 0)]

print(len(sundays))
# Answer: 171
