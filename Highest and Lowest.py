def high_and_low(numbers):
    numbers=numbers.split(' ')
    print(numbers)
    highest=int(numbers[0])
    lowest=int(numbers[0])
    length =len(numbers)
    i=1
    while i<length:
        if int(numbers[i])>highest:
            highest=int(numbers[i])
        elif int(numbers[i])<lowest:
            lowest=int(numbers[i])
        i+=1
    x=(str(highest),str(lowest))
    x=' '.join(x)
    return x
