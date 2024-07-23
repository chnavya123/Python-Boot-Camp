'''for j in range(0,5):
    for i in range(0,j+1):
        print('*',end=" ")
    print('',end='\n')'''    

for j in range(0,5):
    for k in range(0,5-1-j):
        print(' ',end=' ')
    for i in range(0,j+1):
        print('*',end=' ')
    print('',end='\n')
