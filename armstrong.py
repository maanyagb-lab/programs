n= int (input( " Enter the range of numbers "))

for num in range(1, n+1):
    digits = len(str(num))
    s=0
    t=num

    while t>0:
        d = t%10
        s += d ** digits
        t //=10

    if s == num:
        print(num , " is an armstrong number ")
    else:
        print(num , " is not an armstrong number ")
