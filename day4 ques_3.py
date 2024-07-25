#GCD OF 2 NUMBERS:
#UCLIDEAN LGORITHM:
a=int(input("Ënter 1st number: "))
b=int(input("Enter 2nd number:"))
while b!=0:
    a,b=b,a%b
print("GCD of 2 numberds: ",a)