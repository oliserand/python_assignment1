'''
"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing
on long trips, as it has a very repetitive format which is easy to memorize, and can take a long
time to sing. The song's simple lyrics are as follows:
    “99 bottles of beer on the wall, 99 bottles of beer.
    Take one down, pass it around, 98 bottles of beer on the wall.”
    The same verse is repeated, each time with one fewer bottle. The song is completed when the
    singer or singers reach zero.
    Your task here is write a Python program capable of generating all the verses of the song.
'''

counter = 99

while counter > 0:
    if counter != 1:
        print(counter, 
                "bottles of beer on the wall,", counter,
                " bottles of beer.\nTake one down, pass it around,",
                (counter-1), "bottles of beer on the wall.")
    else:
        print(counter, 
                "bottle of beer on the wall,", counter,
                " bottle of beer.\nTake one down, pass it around,",
                (counter-1), "bottle of beer on the wall.")
    counter -= 1
