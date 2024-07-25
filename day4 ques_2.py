#LCM*GCD=a*b
n1=int(input("Ënter 1st number:"))
n2=int(input("Enter 2nd number:"))
while n2!=0:
    n1,n2=n2,n1%n2
    gcd=n1 
print("gcd is:",n1)
print("lcm is:",product//gcd)