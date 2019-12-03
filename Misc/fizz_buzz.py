for num in range(1,20):
    string = ''
    if num % 3 == 0 and num % 5 == 0:
        string = string + 'FizzBuzz'
    elif num % 3 == 0:
        string = string + 'Fizz'
    elif num % 5 == 0:
        string = string + 'Buzz'
    else:
        string = string + str(num)
    print(string , end = ' ')