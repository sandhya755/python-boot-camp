#Password verifiefr mr.x is trying to create a new password instragram account. these are the required conditions for creating a new password
#these are the required conditions for creating a new password
#1.mininum length is =8 max length is =15
#2.only@ , / is allowed in a pass word
#3.No speaces are allowed 
#4.only  alpha numerics are allowed 
#5. your are suppose to print weak if length is excate =8 lenhth is between 8 to 12 strong if length is between 12 to 15
s=input()
n=len(s)
count=0
str="@/"
for i in s:
    if(i==str[0] or i==str[1] and i!=' '):
        count+=1
        break
if(count==0):
   print("please follow the conditions")
elif(n<8):
    print("please follow the conditions")
elif(n==8):
    print("password is weak")
elif(n>=12 and n<15):
    print("password is strong")
else:
    print("very strong")

    #o/p
    #sandhya@123
    #very strong
