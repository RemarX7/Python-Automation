def is_year_leap(num):
    return True if num % 4 == 0 else False


year = int(input('Введите номер года: '))
result_year = is_year_leap(year)
print(f'год {year}: {result_year}')
