'''
Write a program that takes a DNA sequence and returns the number of non-nucleotide bases.
'''

nucleotides = ['a','t','c','g','A','T','C','G']
running = True
while running:
    counter = 0
    dna = input('Enter a DNA sequence: \n')
    if dna == '':
        running = False
    else:
        for nt in dna:
            if nt not in nucleotides:
                counter += 1
        print('DNA sequence contains',counter,'non-nucleotide bases.')
