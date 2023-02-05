from collections import deque


def solution(priorities, location):
    answer = 0
    d = deque([v, i] for i, v in enumerate(priorities))

    while len(d):
        print(d)
        item = d.popleft()
        print(max(d))
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


# def solution(priorities, location):
#     copyList = priorities[:]
#     indexList = [i for i in range(len(priorities))]
#     print(copyList, indexList)
#     result = []
#     index = 0
#     while True:
#         maxV = max(priorities)  # 우선 순위 제일 높은 거


# def solution(priorities, location):
#     # x = [] # 우선순위로 인쇄되는 순서 담는 리스트
#     # array = [i for i in enumerate(priorities)]
#     # print(array)
#     result = [] # 우선 순위 인덱스, 값 담는 리스트
#     index = 0
#     while True:
#         print(">>",priorities[index: len(priorities)])
#         maxV = max(priorities[index: len(priorities)])
#         index = priorities.index(maxV) # 중요도 제일 높은거 인덱스
#         print("maxV:", maxV, "index:",index)
#         result.append([index, maxV])
#         print("result:",result)
#         priorities[index] = None
#         if location == index:

#             return len(result)
#         index += 1
#         print("index:",index)
#
#         if index == len(priorities) - 1: #만약 맨 끝이면 처음으로 이동

#             index = 0


#     print(maxIndex, max(priorities))
#     for idx, v in enumerate(maxIndex, priorities):
#         print(idx, v)


print(solution([2, 1, 3, 2],	2))

# def solution(priorities, location):
#     index = priorities.index(max(priorities)) - 1
#     count = 0
#     while True:
#         if index == len(priorities) - 1:
#             index = 0
#         else:
#             index += 1
#         count += 1
#         if location == index:
#             return count
