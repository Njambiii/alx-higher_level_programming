num = int(input("Please type in a number:"))
n=0
while num>n:
    a = num%10
    num -= a
    num = num/10
    print(a)
    n = n + 1   
print(n)
