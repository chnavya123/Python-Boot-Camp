n=int(input())
m=int(input())
for i in range(n,m+1):
        if i%400==0 or (i%4==0 and i%100!=0):
              print(i,end=" ")
        
