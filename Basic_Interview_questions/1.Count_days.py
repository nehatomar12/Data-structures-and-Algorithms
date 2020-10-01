"""
Given 2 dates get the numbers of days
"""

class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def use_buitin_function(date1, date2):
    from datetime import date
    dt1 = date(date1.year, date1.month, date1.day)
    dt2 = date(date2.year, date2.month, date2.day)
    delta = dt1 - dt2
    print(abs(delta.days))


def without_buitin_function(date1, date2):
    """
    Step1: get list of days in every month
    Step2: count leap year
        1. if current month is less then 2(feb), decrement the year
        2. if year is a multiple of 4 and not multiple of 100. OR year is multiple of 400
            (year % 4 == 0 and year % 100 != 0 or year % 400 ==0)
            int(years/4 - years/100 + years/400)
    Step3: get days
        1. get days( year*365 + days)
        2. count leap year days
        3. count days of months
    """
    months = [31,28,31,30,31,30,31,31,30,31,30,31]

    def _get_leap_year(date):
        if date.month < 2:
            date.year -= 1
        return int(date.year/4 -date.year/100 + date.year/400)

    days1 = date1.year * 365 + date1.day
    # count for leap year
    days1 += _get_leap_year(date1)
    # Add previous month days
    for i in range(0, date1.month-1):
        days1 += months[i]

    days2 = date2.year * 365 + date2.day
    # count for leap year
    days2 += _get_leap_year(date2)
    # Add previous month days
    for i in range(0, date2.month-1):
        days2 += months[i]

    print("Total days: ", abs(days2-days1))
    return (days2-days1)



if __name__ == "__main__":
    date1 = Date(12, 4, 2006 )
    date2 = Date(20, 11, 2005 )
    use_buitin_function(date1, date2)
    without_buitin_function(date1, date2)
