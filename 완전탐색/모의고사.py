def solution(array):
    f = [1, 2, 3, 4, 5]
    s = [2, 1, 2, 3, 2, 4, 2, 5]
    t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(array)):
        if f[i % len(f)] == array[i]:
            count[0] += 1
        if s[i % len(s)] == array[i]:
            count[1] += 1
        if t[i % len(t)] == array[i]:
            count[2] += 1
    max_val = max(count)
    answer = []
    for i in range(3):
        if max_val == count[i]:
            answer.append(i + 1)
    return answer
