# def solution(citations):
#     citations.sort(reverse=True)
#     for i in range(len(citations)):
#         if len(citations[0:i + 1]) >= i+ 1 and i + 1  >= len(citations[i:len(citations)]):
#             return citations[i]

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i+1 > citations[i]:
            break
        answer = i + 1
    return answer


print(solution([3, 0, 6, 1, 5]))
