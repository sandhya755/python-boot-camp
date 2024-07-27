#write a code all the capital letters in a give string 
inp=input()
sum=0
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
      sum+=int(i)
print(sum)