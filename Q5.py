'''
Based in the definition of the mathematical constant e, as the sum of an infinite series
(see wikipedia: http://en.wikipedia.org/wiki/E_%28mathematical_constant%29)
create a program that ask the user for the number of terms used to calculate the approximation, and returns its
value
'''

running = True
while running:
    e = 1
    n = input('Enter number of terms used to approximate e: ')
    if n == '':
        running = False
    else:
        n = int(n)
        for i in range(1,n+1):
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            e += (1/factorial)

        print(e)
