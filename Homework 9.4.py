N = int(input("Enter N: "))
A = []
A_reversed = 0

for i in range(N):
    N_number = int(input("Enter your number: "))
    A.append(N_number)
    A_reversed = A[::-1]

print(A_reversed)
