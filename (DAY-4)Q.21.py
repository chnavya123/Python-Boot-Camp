#peak element
'''my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        #count=i
        print(my_list[i],end=" ")'''

#sort elements first half in ascending order and next in descending order
'''my_list=list(map(int,input().split(" ")))
my_list.sort()
print(my_list)'''

my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        count=i
if(my_list[-1]>my_list[-2] and my_list[-1]>count):
    count=len(my_list)-1
print(my_list[count])    







