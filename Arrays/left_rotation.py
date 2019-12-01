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


