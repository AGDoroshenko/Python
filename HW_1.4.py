i = int(input('Введите число:'))
ls = []
while i > 10:
    ls.append(i % 10)
    i //= 10
r = max(ls)
print(f"Самая большая цифра равна {r}.")