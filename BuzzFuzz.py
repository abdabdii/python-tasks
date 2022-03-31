def printValue(number):
    if number %6 ==0 and number %4 == 0:
        return ''
    elif number%4 ==0:
        return 'Fizz'
    elif number%6 == 0:
        return 'Buzz'
    
    return number

for i in range(1,100):
    print(printValue(i))
