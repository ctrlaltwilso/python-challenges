# Challenge: create a function that adds days to a date.
# Must account for leap years.

def is_leap_year(year):
    leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True

    return leap_year

def add_days(date, n):
    '''input date: YYYY-MM-DD, add days(n) and will include leap years'''
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # break down input string into year, month day
    format_elements = [int(part) for part in date.split("-")]
    print("format elements: ", format_elements)

    # store elements as variables
    year = format_elements[0]
    month = format_elements[1]
    days = format_elements[2]

    while n > 0:
        # check for leap year
        if is_leap_year(year):
            days_in_month[2] = 29
        else:
            days_in_month[2] = 28
            
        days_left = days_in_month[month] - days

        # add days and subtract n value
        if n <= days_left:
            days += n
            break
        else:
            n -= days_left + 1
            days = 1

            if month >= 12:
                month = 1
                year += 1
            else:
                month += 1
                
    return f"{year:04d}-{month:02d}-{days:02d}"

print(add_days('1999-01-01', 365))