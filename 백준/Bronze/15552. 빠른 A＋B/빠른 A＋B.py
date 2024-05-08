import sys

input_num = int(sys.stdin.readline())

num = []

for i in range(input_num):
    num.append(sys.stdin.readline().split())

for j in range(input_num):
    print(int(num[j][0]) + int(num[j][1]))