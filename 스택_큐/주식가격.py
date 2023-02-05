# def solution(prices):
#     result = []
#     for i in range(len(prices)):
#         count = 0
#         endIndex = 0
#         for j in range(i, len(prices)): # 현재 시점부터
#             print(prices[i] , prices[j])
#             endIndex = j
#             if j == len(prices) - 1:
#                 break
#             if prices[i] > prices[j]:  # 가격이 떨어지면
#
#                 print("endIndex" , endIndex)
#                 break
#                 # result.append(len(prices[i:j]))
#                 # break
#         if endIndex == 0 and  :
#             result.append(len(prices[i:endIndex]))
#
#         count += 1


    # return result

def solution(prices):
    result = []
    for i in range(len(prices)):
        curIndex = i
        while curIndex != len(prices)-1:
            if prices[i] > prices[curIndex]:
                break
            curIndex += 1
        result.append(curIndex - i)
    return result





print(solution([1, 2, 3, 2, 3]))