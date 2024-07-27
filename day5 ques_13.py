inp=input()
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=57):#65 to 90 are capital letters
       sum+=int(i)
print(sum)