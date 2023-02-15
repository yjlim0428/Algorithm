# def solution(citations):
#     citations.sort(reverse=True)
#     for i in range(len(citations)):
#         if len(citations[0:i + 1]) >= i+ 1 and i + 1  >= len(citations[i:len(citations)]):
#             return citations[i]


def solution(citations):
    answer = 0
    citations = sorted(citations) # 오름차순 정렬
    for idx, paper in enumerate(citations):
        print(idx,paper)
        if paper >= len(citations[idx:]):
            answer = len(citations[idx:])
            break

    return answer

print(solution([3, 0, 6, 1, 5]))
