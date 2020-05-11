# Задание №1
Работа_на_удаленке = input('Вы работает на удаленке - да, нет? ')

if Работа_на_удаленке == "да":
    print('Вам относительно повезло')
    Время_работы_на_удаленке = input('Сколько вы работаете дней? ')
    print(f'Вы молодец, отработали {Время_работы_на_удаленке} дней')
else:
    print('Мы вам сочувствуем')

# Задание №2
seconds = int(input('Введите время в секундах '))
hours = int(seconds // 3600)
seconds2 = int((seconds % 3600) % 60)
minuts = int((seconds % 3600 - seconds2) / 60)
if hours < 10:
    fomat_hours = "0"
else:
    fomat_hours = ""
if minuts < 10:
    format_minut = "0"
else:
    format_minut = ""
if seconds2 < 10:
    format_seconds = "0"
else:
    format_seconds = ""
print(f"{fomat_hours}{hours} : {format_minut}{minuts} : {format_seconds}{seconds2}")

# Задание №3
chislo = input('Введите число от 1 до 9 ')
n = chislo
nn = chislo+chislo
nnn = chislo+chislo+chislo
print(f"{n} {nn} {nnn}")
n = int(n)
nn = int(nn)
nnn = int(nnn)
sum = n + nn + nnn
print(sum)

# Задание №4
число = int(input('Введите число '))
x = число % 10
число = число // 10
z = число % 10
while число > 0:
    if x >= z:
        число = число // 10
        z = число % 10
    else:
        x = z
        continue

print(f'Максимальная цифра в числе = {x} ')

# Задание №5
revenue = int(input('Введите выручку компании '))
costs = int(input('Введите расходы компании  CAPEX/OPEX '))
margin = revenue - costs
if margin > 0:
    margin_percent = margin / revenue * 100
    ССЧ = int(input('Введите среднесписочную численность сотрудников '))
    print(f"Рентабельность фирмы = {margin_percent}%")
    margin_per_person = margin / ССЧ
    print(f"Прибыль фирмы в расчете на одного сотрудника = {round(margin_per_person,2)} рублей.")
elif margin == 0:
    print('Компания покрывает себестоимость и прочие издержки')
else:
    print(f'Компания работает в убыток в размере {margin} рублей.')

# Задание №6
result = int(input("Введите результат первого дня пробежек в км. "))
goal = int(input("Введите желаемый результат в км. "))
days = 1
print(f"Результат в {days}-й день составит {round(float(result),2)} км.")
while result <= goal:
    result = result + (result * 0.1)
    days = days + 1
    print(f"Результат в {days}-й день составит {round(float(result),2)} км.")

print(f"На {days}-й день вы достигнете результат не менее {int(result)} км.")
