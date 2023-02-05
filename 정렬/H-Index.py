def solution(citations):
    citations.sort(reverse=True)
    print("citations:",citations)
    for i in range(len(citations)):
        print(citations[0:i + 1], citations[i:len(citations)])
        if len(citations[0:i + 1]) >= i+ 1 and i + 1  >= len(citations[i:len(citations)]):
            return citations[i]


print(solution([7]))
