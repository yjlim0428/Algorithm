from collections import deque


def solution(bridge_length, weight, truck_weights):
    result = bridge_length
    truckList = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])  # 다리 위에 있는 트럭
    bridgeSum = 0
    while len(truckList) != 0:

        bridge.popleft()

        if bridgeSum + truckList[0] <= weight:  # 올라갈 트럭이랑 다리 위에 트럭들 합을 다리가 버틸 수 있으면
            bridge.append(truckList[0])  # 추가
            bridgeSum += truckList[0]
            truckList.popleft()

        else:
            bridge.append(0)

        if bridge[0] != 0:
            bridgeSum -= bridge[0]

        result += 1
    return result


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
