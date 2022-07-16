kg = int(input())
result = 0


while kg > 0:
    if kg >= 5 & (kg + 5) % 3 != 0:
        kg -= 5
        result += 1
        # if kg - 5 >= 5: 

        # elif (kg + 5) % 3 == 0:
        #     kg += 5
        #     result -= 1
    elif kg >= 3:
        kg -= 3
        result += 1
    else: 
        result = -1
        break
    
    # print(">>",kg)

print('reuslt>', result)
        

