#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

string = "sikandar"


def stringbits(string):
    b = ""
    i = 0
    while i < len(string):
        b += string[i]
        i = i+2
    return b


print(stringbits(string))
