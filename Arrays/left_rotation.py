# A left rotation operation on an array shifts each of the array's elements  unit to the left.
# input paraeters : 
# An array of integers - a
# An integer d the number of rotations.

def rotLeft(a , d):
    l = len(a)
    tempArr = []
    counter = 0
    for i in range(d,l):
        tempArr.append(a[i])
        counter +=1
    for j in range(0,d):
        tempArr.append(a[j])
    return tempArr
userArray = [1,2,3,4,5]
print(rotLeft(userArray,2))

###### Optimised solution #######

def rotLeft1(a,d):
    l = len(a)
    tempArr1 = []
    newIndex = 0
    for i in range(0,l):
        newIndex = (i+d) % l
        tempArr1.append(a[newIndex])
    return tempArr1

userArray1 = [1,2,3,4,5]
print(rotLeft1(userArray1,2))
