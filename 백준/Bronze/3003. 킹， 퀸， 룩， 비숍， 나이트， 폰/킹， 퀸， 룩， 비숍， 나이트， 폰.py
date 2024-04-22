data = list(map(int, input().split()))
ref = [1, 1, 2, 2, 2, 8]
for i in range(len(data)):
    print(f"{ref[i] - data[i]}", end="")
    if i != len(data) - 1:
        print(" ", end="")