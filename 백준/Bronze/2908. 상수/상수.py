import sys

def solution(input):
    a, b = map(str, input.split())
    a, b= int(a[::-1]), int(b[::-1])
    return a if a > b else b
    
print(solution(sys.stdin.readline()))