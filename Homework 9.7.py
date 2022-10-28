N = input("Введите текст: ")
A = []

for symbol in N:
    if symbol.isdigit():
        A.append(symbol)
    else:
        continue

print("Количество цифр:", len(A))
