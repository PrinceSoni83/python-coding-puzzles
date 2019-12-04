def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
        
user_input = input("Enter the number for factorial: ")
print("Recursive value: ", fact(int(user_input)))