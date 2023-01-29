def solution(nums):
    # return len(set(nums)) if len(set(nums)) < len(nums) / 2 else len(nums) // 2
    return min(len(nums)/2, len(set(nums)))

print(solution([3,3,3,2,2,2]))