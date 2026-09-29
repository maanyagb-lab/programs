n= int(input(" Enter a number "))
reverse = 0
t=n

while t>0:
    d = t%10
    reverse = reverse * 10 + d
    t//=10

if reverse == n:
    print(n, " is a palindrome number ")
else:
    print(n, " is not a palindrome number ")

