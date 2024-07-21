#find the missing number in an array
#1 2 3 4 5 6 7 8 9 10 ===55
#1 2 3 4 5 7 8 9 10====49
#6
'''arr=[1,2,3,4,6,7,8,9,10]
s=0
for i in range(1,len(arr)+1):
    s=s+i
e=50-s
print(e)'''

#15.find the duplicates in an array 
'''my_list=list(map(int,input().split(" ")))
list=[]
for i in my_list:
    if(i not in list):
        list.append(i)
print(list) '''

#sum of digits:123  1+2+3=6
'''n=1234444
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)  '''    

#find the sum of the squares of the digits
n=338633
sum=0
while n>0:
    r=n%10
    if(n%2==0):
        sum=sum+r
    n=n//10
print(sum) 

#123
#321
n=123
s=""
while n>0:
    r=n%10
    s=s+str(r)
    n=n//10
print(s)
 
