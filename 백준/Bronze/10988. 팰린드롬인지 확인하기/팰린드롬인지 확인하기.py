word = input()
N = len(word)
count = 0
for i in range(int(N/2)):
    if word[i] == word[N-1-i]:
        count += 1
if count == int(N/2):
    print(1)
else:
    print(0)