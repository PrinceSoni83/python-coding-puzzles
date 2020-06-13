# k-1 for pyramid , k-2 for 180 degree inverted tringle
n = int(input("Enter the count of rows you want in pyramid : "))
def pyramid(n):
    k = 2*n - 1
    for j in range(0,n):
        for i in range(0,k):
            print(end=" ")
        k = k - 1
        for i in range(0, j+1):
            print("* ",end="")
        print()
pyramid(n) 