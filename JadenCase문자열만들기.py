#프로그래머스

def solution(s):

    return ' '.join([word.capitalize() for word in s.split(" ")])


    # return s.title()


    # result = ""
    # for i in range(len(s)):
    #     if s[i] == " ":
    #         result += " "
    #     else:
    #         if i == 0:
    #             result += s[0].upper()
    #         elif s[i-1] == " ":
    #             result += s[i].upper()
    #         else:
    #             result += s[i].lower()
    #
    # return result

print(solution("3people unFollowed      me"))