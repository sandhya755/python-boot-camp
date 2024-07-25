#print the element in a particular index using cyclic printing.
my_list=list(map(int,input().split(" ")))
k=int(input())
#for i in range(0,len(my_list)):
     #if(i==k):
     #print(my_list[k])
     #break
#if(k>len(my_list)):
n=k%(len(my_list))
     ##n=k-len(my_list)
print(my_list[n])