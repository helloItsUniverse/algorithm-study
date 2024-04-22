N = int(input())
for i in range(-(N - 1), N):
    for j in range(abs(i)):
        print(" ", end="")
    for K in range(1, 2*N - 2*abs(i)):
        print("*", end="")
    print()