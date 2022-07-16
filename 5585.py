money = int(input())
money = 1000 - money
result = 0
moneyList = [500, 100, 50, 10, 5 ,1]
index = 0
while money != 0 :
    if( money>= moneyList[index]):
        money -= moneyList[index]
        result += 1
    else: 
        index += 1

print(result)

