num = int(input("enter the number to reverse: "))
def reverse_a_number(num):
    rev = 0
    while num > 0:
        digit =  (num % 10)
        rev = rev * 10 + digit
        num  = num // 10
    return rev
print('Given number is : ', num)
print('Reverse of given number is :', reverse_a_number(num))
