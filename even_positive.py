num=int(input("Enter the number:\n"))
if(num%2==0 and num>0):
   print(f"{num} is positive even number")
elif(num%2==0 and num<0):
    print(f"{num} is negative even number")
else:
    print(f"{num} is positive odd number")