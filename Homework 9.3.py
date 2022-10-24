A = []

for i in range(10):
    number = int(input(f"Enter your number #{i + 1}: "))
    A.append(number)

print(A)

N = int(input("Enter number N: "))

print("N consists in A", A.count(N), "time(s)")
