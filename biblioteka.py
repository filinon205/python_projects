z = input("script_name")
x = input("норма_час")
q = input("часы")
s = input("РК_и_СН")
a = input("Процент_премии")

lis = [z, x, q, s, a]
for z, i in enumerate(lis):
    i = int(lis[z])
    print(i, end= " ")