num = input("Enter the number : ")
num = int(num)

for i in range(1,num+1):
    if (i == 4 or i == 13):
        state = "unlucky"
    elif i%2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{i} is {state}")
    