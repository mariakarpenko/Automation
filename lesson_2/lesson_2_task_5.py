def month_to_season(m):
    
        if (1 <= m <= 2 or m == 12):
            print("Это зимний месяц")
        elif (3 <= m <= 5):
            print("Это весенний месяц")
        elif (6 <= m <= 8):
            print("Это летний месяц")
        elif (9 <= m <= 11):
            print("Это осенний месяц")
        else:
             print("Это не месяц")
             

month_to_season(72)