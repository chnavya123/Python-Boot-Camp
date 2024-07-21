#find the maximum element in the given list
#test case:0
#12 23 36 44 45 57
#57
#------
'''test case:1   56 78 -8 12 34 -99  --- 78'''
'''my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)  '''


#12.find the min element in the given list
'''my_list=list(map(int,input().split(" ")))
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
print(min)  '''

#replace the elements in an array with average of maximum and minimum element
#13 2 67 20 68  #68+2=70==35  #35 35 35 35 35
my_list=list(map(int,input().split(" ")))
min=my_list[0]
max=my_list[0]
avg=0
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
for j in range(len(my_list)):
    if(my_list[j]<min):
        min=my_list[j]
avg=(max+min)//2        
for i in range(len(my_list)):
    my_list[i]=avg              
print(avg)    
print(my_list)    




