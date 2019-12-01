def isReverse(usrInput):
    reverseStr = []
    length = len(usrInput)
    if length == 1 :
        return "Palindrom"
    elif usrInput == '':
        print("please input the string", end='/n')
    else:
        while length > 0:
            reverseStr += usrInput[length-1]
            length -= 1
        revString = ''.join(reverseStr)
        if usrInput == revString:
            return "Palindrom"
        else:
            return "Not a Palindrom"
usrInput = input("Input the string to check: ")
print(isReverse(usrInput))


