def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i][0:len(phone_book[i-1])] == phone_book[i-1]:
            return False
    return True


print(solution(["123","456","789"]))
