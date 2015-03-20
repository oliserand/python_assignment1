'''
A pangram is a sentence that contains all the letters of the English alphabet at least once, for
example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to
check a sentence to see if it is a pangram or not.
'''

sentence = "The quick brown fox jumps over the lazy dog"
sentence_lower = sentence.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
uniq = []
for letter in sentence_lower:
    if (letter in alphabet) and (letter not in uniq) and (letter != ' '):
        uniq.append(letter)
        
if len(uniq) == 26:
    print('Sentence is a pangram.')
else:
    print('Sentence is not a pangram.')
