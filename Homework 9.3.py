A = []

for i in range(10):
    number = int(input("Enter your number: "))
    A.append(number)

print(A)

N = int(input("Enter number N: "))

print("N consists in A", A.count(N), "time(s)")
