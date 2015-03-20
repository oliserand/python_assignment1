'''
Create a program that calculates the factorial of a number n entered by the user.
'''

factorial = 1
running = True
while running:
    number = input('Enter a number: ')
    if number == '':
        running = False
    else:
        number = int(number)
        for i in range(1, number+1):
            factorial *= i

        print(factorial)
    factorial = 1
