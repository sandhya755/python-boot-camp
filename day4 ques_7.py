#peak element
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if (my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]):
        count=i
        break
print(my_list[count])
# o/p
#5 12 8 17 -2
#12