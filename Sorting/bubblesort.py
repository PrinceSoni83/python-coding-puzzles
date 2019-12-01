input = input("Enter comma seperated values: ")
defArr = input.split(",")
for i in range(0,len(defArr)-1):
    for j in range(i,len(defArr)-1):
        swap = True
        temp = 0
        if defArr[j] > defArr[j+1]:
            temp = defArr[j]
            defArr[j] = defArr[j+1]
            defArr[j+1] = defArr[j]
            swap = False
        if(not swap):
            break
print(defArr)