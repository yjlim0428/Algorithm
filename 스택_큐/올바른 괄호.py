def solution(s):
    if s[0] == ")":
        return False
    else:
        count = 0;
        for i in s:
            if i == "(":
                count += 1
            if i == ")":
                count -= 1
            if count < 0:
                return False
    return count == 0




print(solution("()()"))