'''
Write a program that ask the user to input a text and then recognises palindromes (i.e. words
that look the same written backwards). For example, "radar" is a palindrome.
'''


running = True
while running:
    text = input('Input a text: \n')
    if text == '':
        running = False
    else:
        print(text[::-1])
