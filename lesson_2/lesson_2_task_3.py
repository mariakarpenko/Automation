def square(a):
    import math

    if (a % 1 == 0):
        area = a * a
        print(area)
    else:
        round_num = math.ceil(a)
        rounded_area = round_num * round_num
        print(rounded_area)

square(7)