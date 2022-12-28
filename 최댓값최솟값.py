#프로그래머스


def solution(s):
    intList = list(map(int, s.split(" ")))
    return str(min(intList)) + " " + str(max(intList))


print(solution("-1 -2 -3 -4"))

