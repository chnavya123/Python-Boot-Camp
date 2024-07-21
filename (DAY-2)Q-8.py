'''given the space separated integer list. find the average of elements present in the even index.'''
my_list=list(map(int,input().split(" ")))
#average=0
sum=0
'''for i in range(0,len(my_list),2):
    if(i%2==0):
        sum+=my_list[i]
        average=sum/len(my_list)
print(average)'''
count=0
n=len(my_list)
for i in range(len(my_list)):
    sum+=my_list[i]
    count+=1
print(sum/count)

