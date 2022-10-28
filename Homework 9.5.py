# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

A = []
C = []

for i in range(5):
    numbers = int(input(f"Enter your number #{i + 1}: "))
    A.append(numbers)

for y in A:
    if y > 5:
        C.append(y)
    else:
        continue

print(C)
