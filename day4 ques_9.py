#prime number
a=int(input("Ënter a number:"))
r=a**0.5
count=0
if a==1:
    print("Not a primre number")
elif a==2:
    print("prime number")
for i in range(2,int(r+1)):
    if(a%i==0):
        count=1
        break
if count==0:
   print("prime")
else:
    print("not a prime")