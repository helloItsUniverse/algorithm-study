import sys

def solution(input):
    time = 0
    for i in input:
        if ord(i) <= ord('Z') and ord(i) >= ord('W'):
            time += 10
        elif ord(i) <= ord('V') and ord(i) >= ord('T'):
            time += 9
        elif ord(i) <= ord('S') and ord(i) >= ord('P'):
            time += 8
        elif ord(i) <= ord('O') and ord(i) >= ord('M'):
            time += 7
        elif ord(i) <= ord('L') and ord(i) >= ord('J'):
            time += 6
        elif ord(i) <= ord('I') and ord(i) >= ord('G'):
            time += 5
        elif ord(i) <= ord('F') and ord(i) >= ord('D'):
            time += 4
        elif ord(i) <= ord('C') and ord(i) >= ord('A'):
            time += 3
    return time
    
print(solution(sys.stdin.readline()))