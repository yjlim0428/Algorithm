
n=int(input())
pList =list(map(int, input().split(" ")))
pList.sort()

result=0;
x=0;
for i in pList:
  x+=i
  result+= x
print(result)

