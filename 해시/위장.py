def solution(clothes):
    clothDic = {}
    for i, j in clothes:
        if j not in clothDic.keys():
            clothDic[j] = [i]
        else:
            clothDic[j].append(i)

    result = 1
    for k, v in clothDic.items():
        result *= len(v) + 1

    return result - 1




print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))#5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	))#3