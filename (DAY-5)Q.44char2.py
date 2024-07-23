#remove all the brackets from the given algebraic expression.
n=input()
for i in n:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93):
        pass
    else:
        print(i,end="")
print()        

