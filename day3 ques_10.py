#find the element present in (k+n)th index.k is given by user.
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
leng=len(my_list)
if(len<k+n):
    print("ERROR")
else:
    for i in range(0,len(my_list)):
        print(my_list[k+n],end=" ")
        break
    #for i in range(leng):
         #if(i==k+n):
         #print("the element present in the (k+n)th position is:",my_list[i])

