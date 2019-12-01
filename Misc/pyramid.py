n = int(input("Enter the count of rows you want in pyramid : "))

for i in range(1,n+1):
    for j in range(1,(n*2)-1):
        if(j >= n-(i-1) and j<= n+(i-1)):
            print("*",end=" ")
        else:
            print(end =" ")
    print(end='\n')
# for row in range(n):
#         for col in range(n-row-1):
#             print(end=" ")
#         for col in range(row+1):
#             print("*", end=" ")
#         print()
