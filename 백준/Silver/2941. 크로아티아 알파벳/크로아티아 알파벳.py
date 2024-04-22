line = list(input())
for i in range(len(line)):
    if line[i] == "=":
        if line[i - 1] == "c" or line[i - 1] == "s":
            line[i] = line[i - 1] + line[i]
            line[i - 1] = " "
        elif line[i - 1] == "z":
            line[i] = line[i - 1] + line[i]
            line[i - 1] = " "
            if line[i - 2] == "d":
                line[i] = line[i - 2] + line[i]
                line[i - 2] = " "
    elif line[i] == "-":
        if line[i - 1] == "c" or line[i - 1] == "d":
            line[i] = line[i - 1] + line[i]
            line[i - 1] = " "
    elif line[i] == "j":
        if line[i - 1] == "l" or line[i - 1] == "n":
            line[i] = line[i - 1] + line[i]
            line[i - 1] = " "
            
count = 0
for elem in line:
    if elem != " ":
        count += 1
print(count)