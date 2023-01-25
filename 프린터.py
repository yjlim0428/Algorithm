def solution(priorities, location):
    result = []
    idx = 0
    while len(result) != priorities:
        maxNum = max(priorities)
        # print("maxNum : ", maxNum, )
        for i in range(idx, len(priorities)):
            print(priorities[i],"idx:", idx)
            if maxNum == priorities[i]: # 제일 큰 값이랑 이번 순서 값이랑 같으면
                if location == i:
                    return len(result)  + 1
                else:
                    idx = i  # 제일 큰 값 인덱스 저장
                    if idx == len(priorities) - 1:
                        idx = 0
                result.append(i) # 인덱스를 결과 리스트에 추가
                priorities[i] = 0



print(solution([2, 1, 3, 2], 2))