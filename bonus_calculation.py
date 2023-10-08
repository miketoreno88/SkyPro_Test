def calculate_bonus(years_worked, annual_income, took_sick_leave):
    bonus_percentage = 0
    
    if years_worked > 3:
        bonus_percentage = 30.0
    elif years_worked >= 1.5:
        bonus_percentage = 25.0
    elif years_worked >= 0.25:
        bonus_percentage = 15.0

    if not took_sick_leave:
        bonus_percentage += 3.0

    bonus = (annual_income * bonus_percentage) * 0.01
    return bonus


print(calculate_bonus(3, 50000, False))