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
