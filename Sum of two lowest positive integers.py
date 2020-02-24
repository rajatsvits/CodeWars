Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

#best
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

#Even works array having negative numbers
def sum_two_smallest_numbers(n):
    x=n[1]
    y=n[0]
    i=2
    while i<len(n):
        print(n[i])
        if n[i]>0 and (y>n[i] or x>n[i]):
            if y>x:
                y=x
                x=n[i]
            else:
                x=n[i]
        i+=1
    print(x,y)
    return (x+y)
    #your code here
