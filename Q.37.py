'''n=(input())
for i in n:
    n=ord(i)+4
    print(chr(n),end="")'''

#XYZ
#BCD
n=input()
for i in n:
    n=ord(i)+3
    if n>=90:
        print(chr(n-25))
    else:
        print(chr(n))    


    
    