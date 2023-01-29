def solution(progresses, speeds):
    import math
    day = []
    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i]) / speeds[i]))
    result = []
    print(day)
    d = 0
    for i in day:
        if i > d:
            result.append(1)
            d = i
        else:
            result[-1] += 1
    return result

print(solution([93, 30, 55], 	[1, 30, 5]))

