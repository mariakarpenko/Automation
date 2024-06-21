is_year_leap = input('Year: ')
is_year_leap_int = int(is_year_leap)

if (is_year_leap_int % 4 == 0):
    print("Year" + is_year_leap + ": " + "Leap")
else:
    print("Year " + is_year_leap + ": " + "Non-leap")