N = int(input("Enter N: "))
A = []

for i in range(N):
    N_numbers = int(input(f"Enter your number №{i + 1}: "))
    A.append(N_numbers)
    A.sort()

print("Minimum:", A[0])
print("Maximum:", A[-1])
