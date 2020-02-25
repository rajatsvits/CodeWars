Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


#Best
def countBits(n):
    return bin(n).count("1")

#Mine
def countBits(x):
    c=0
    n=x
    while n>0:
        if n%2==1:
            c+=1
        n=int(n/2)
#         print(n,c)
    return c
#     return [count(c) if x==1 while n%2==1: n=n/2]
