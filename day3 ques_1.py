#dublicants ,#find duplicates in an array
#8 7 7 8 5 4 4 8 9
n=list(map(int,input().split()))
a=[]
for i in n:
    if(i not in a):
        a.append(i)
print(a)