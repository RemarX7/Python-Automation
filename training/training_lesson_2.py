# students: list[str] = ['Kolya', 'Vasya', 'Sveta', 'Vera', 'Nika', 'Dusya', 'Lusya']
# for x in range(0, len(students)):
#     print(students[x])

# word = 'TECTOCTEPOH'
# for w in word:
#     print(w)

# for stud in students:
#     print(stud)
# #Вывод списков с циклами (3 способа) 

# employee_list: list[str] = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
# print(employee_list[1] + ', ' + employee_list[-2])
# #2 и 2-ой с конца 

def dev_by_three(number):
    return "Да" if number % 3 == 0 else "Нет"

num = int(input("Введите число: "))
result = dev_by_three(num)
print(f"Делится ли на три {num}? - {result}")

# import math
# def min_boxes(items):
#     return math.ceil(items / 5)
# num_items = int(input('Введите кол-во предметов: '))
# print(f'Максимальное кол-во коробок: {min_boxes(num_items)}')

# Напишите функцию check_divisibility, которая принимает одно число — n — и выводит все числа от 1 до n (включительно):
# Если число делится на 2, но не на 4, оно выводится с текстом «Делится на 2, но не на 4».
# Если число делится и на 2, и на 4, оно выводится с текстом «Делится и на 2, и на 4».
# Все остальные числа выводятся просто как есть

# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if i % 2 == 0 and i % 4 != 0:
#             print(f"{i} — Делится на 2, но не на 4")
#         elif i % 2 == 0 and i % 4 == 0:
#             print(f"{i} — Делится и на 2, и на 4")
#         else:
#             print(i)

# n = int(input('Введите число'))
# check_divisibility(n)

# Напишите функцию 
# quarter_of_year()
# , которая принимает один аргумент — номер месяца (от 1 до 12) — и возвращает номер квартала, к которому относится этот месяц.
# Например, если передать 5, на выходе должно быть 
# II квартал
# , так как май относится ко второму кварталу.

def quarter_of_year(month):
    if 1 <= month <= 3:
        return "I квартал"
    if 4 <= month <= 6:
        return "II квартал"
    if 7 <= month <= 9:
        return "III квартал"
    if 10 <= month <= 12:
        return "IV квартал"
    return "Неверный номер месяца"

month = int(input("Введите номер месяца (1-12): "))
print(quarter_of_year(month))

# Дан список 
# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
# .
# Необходимо вывести элементы, которые одновременно:
# больше 15,
# делятся на 3 без остатка.

# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
# for i in lst:
#     if i > 15 and i % 3 == 0:
#         print(i)

# for i in range(25, 0, -5):
#     print(i)

var_1 = 50
var_2 = 5 
var_1, var_2 = var_2, var_1
print(var_1, '- 1', var_2, '- 2')