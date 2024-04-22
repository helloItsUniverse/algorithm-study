contents = list()
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for content in contents:
    print(content)