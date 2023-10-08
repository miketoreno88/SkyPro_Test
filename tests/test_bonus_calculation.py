import pytest
from bonus_calculation import calculate_bonus

@pytest.mark.parametrize("years_worked, annual_income, took_sick_leave, expected_bonus", [


    (10, 50000, False, 16500.0),
    (1.7, 60000, True, 15000.0),
    (1, 70000, False, 12600.0),

    # Случаи для "от 1.5 до 3 лет работы"
    (3, 50000, False, 14000.0),
    (2.99, 60000,False, 16800.0),
    (3.01, 70000, False, 23100.0),

    # Случаи для "от 90 дней до 1.5 лет работы"
    (1.5, 50000, False, 14000.0),  # Граничное значение: Работа точно 1.5 года
    (1.49, 60000, False, 10800.0), # Близкое к граничному значению снизу: Работа 1.49 года
    (1.51, 700000, False, 196000.0), # Близкое к граничному значению сверху: Работа 1.51 года

    # Случаи для "менее 90 дней работы"
    (0.25, 50000, True, 7500.0),  # Граничное значение: Работа точно 90 дней
    (0.24, 60000,True, 0.0),  # Близкое к граничному значению снизу: Работа 0.24 года
    (0.26, 70000, True, 10500.0)  # Близкое к граничному значению сверху: Работа 0.26 года
])
def test_calculate_bonus(years_worked, annual_income, took_sick_leave, expected_bonus):
    result = calculate_bonus(years_worked, annual_income, took_sick_leave)
    assert result == expected_bonus
