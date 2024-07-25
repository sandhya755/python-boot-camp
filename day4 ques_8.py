#prime numbers in range
a=int(input("ënter the 1st number"))
b=int(input("enter the 2nd number"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)