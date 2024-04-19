def solution(name, yearning, photo):
    answer = []
    i = 0
    result = 0
    for p in photo:
        for pp in p:
            # print(pp)
            for n in name:
                # print(n)
                if pp == n:
                    result += yearning[i]
                i += 1
            i = 0
        answer.append(result)
        result = 0 # result initialize
    return answer