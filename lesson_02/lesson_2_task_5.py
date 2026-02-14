def month_to_season(num_month):
    if 1 <= num_month <= 2 or num_month == 12:
        return 'Зима'
    elif 3 <= num_month <= 5:
        return 'Весна'
    elif 6 <= num_month <= 8:
        return 'Лето'
    elif 9 <= num_month <= 11:
        return 'Осень'
    return "Неверный номер месяца"


num_month = int(input('Введите номер месяца (1-12): '))
print(month_to_season(num_month))
