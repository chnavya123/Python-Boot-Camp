'''n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    #for j in range(2*i+1):
    # print("*",end="")    
    for j in range(i+1):
        print("*",end=" ")
    print() '''

'''n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(i):
        print(" ",end="")    
    for j in range(2*(n-i)-1):
        print("*",end="")
    print()'''

'''n=int(input("enter a number:"))
for i in range(1,n+1):
    print((n-i) * ' ' + (2*i-1) * '*')
for x in range(1,n):
    print(x * ' ' + (2*(n-x)-1) * '*')'''

'''row=int(input("enter the number of rows:"))
for i in range(row):
    print(" "*(row-i)+" *"*(row+1))'''


