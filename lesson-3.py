# # задание1
# def my_funct1():
#     try:
#         arg1 = int(input("Введите числитель "))
#         arg2 = int(input("Введите знаменатель "))
#         chastnoe = arg1 / arg2
#         print(f"Результат: {float(chastnoe)}")
#     except ZeroDivisionError:
#         return print("Деление на 0 невозможно, введите целое число")
#
#
# print(my_funct1())
#
#
# # задание 2
#
# def my_func2(Name, Surname, Birthday, city, mail, tel):
#     print(f"Name: {Name}; Surname: {Surname}; Birthday: {Birthday}; city: {city}; mail: {mail}; tel: {tel}")
#
#
# my_func2(Name=input("Введите имя "), Surname=input("Введите Фамилию "), Birthday=input("Введите Год рождения "),
#          city=input("Введите Город "), mail=input("Введите Почту "), tel=input("Введите Телефон "))
#
# задание
# 3
#
#
# def my_fun3(arg1, arg2, arg3):
#     список = list(arg1)
#     список.append(arg2)
#     список.append(arg3)
#     список.sort(reverse=True)
#     chisl1 = int(список[0])
#     chisl2 = int(список[1])
#     summa = chisl1 + chisl2
#     print(f"Сумма наибольших аргуметов = {summa}")
#
#
# my_fun3(input("Введите число 1 "), input("Введите число 2 "), input("Введите число 3 "))
#
#
# # задание 4
# def my_fun4(arg1, arg2):
#     stepen = arg1 ** arg2
#     print((f"Число = {stepen}"))
#
#
# my_fun4(arg1=float(input("Введите положительное число 1 ")), arg2=float(input("Введите отрицательное число 2 ")))

# Задание 5 не доделал


def my_fun5(лист1):
    global z
    z = 0
    for y, i in enumerate(лист1):
        try:
            i = int(лист1[y])
            values = None
        except ValueError:

            лист1.remove(i)
            values = 'q'

    for y, i in enumerate(лист1):
        i = int(лист1[y])
        z = z + i
        summa = z
    return summa, values

values = None
список = list()
while values != "q":
    values = input("Введите значения через пробел, для выхода нажмите q  ")
    if values == "q":
        break
    else:
        лист1 = list(values.split(" "))
        vivod, values = my_fun5(лист1)
        vivod = str(vivod)
        список.append(vivod)
        podschet = 0
        for schet, cht_to in enumerate(список):
            cht_to = int(список[schet])
            podschet = podschet + cht_to

        print(podschet)

