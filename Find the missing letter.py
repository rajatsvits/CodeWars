Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)
#Best
def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
    
def find_missing_letter(chars):
    return set(chr(i) for i in range(ord(chars[0]), ord(chars[-1]) + 1)).difference(set(chars)).pop()

def find_missing_letter(chars):
    return (set(charset[ord(chars[0]):ord(chars[-1])+1]) - set(chars)).pop()
    
def find_missing_letter(chars):
    return [c for c in charset[ord(chars[0]):ord(chars[-1])+1] if c not in chars][0]    
    
#Mine
def find_missing_letter(chars):
    missing=' '
    for i in range(1,len(chars)):
        if(ord(chars[i])-ord(chars[i-1])!=1):
            missing=chr(ord(chars[i])-1)
    return missing
#     return [i if (ord(chars[i])-ord(chars[i-1])!=1) for i in range(1,len(chars))]
