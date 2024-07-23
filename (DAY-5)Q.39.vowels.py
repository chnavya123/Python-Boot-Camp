#print no. of vowels in a string
'''check=['a','e','i','o','u']
count=0
inp="hello world"
for i in inp:
    if(i in check):
        count+=1
print(count) '''


'''count=0
con=0
inp="nAvya"
inp=inp.lower()
for i in inp:
    if(i in "aeiou"):
        count+=1
    elif i in "bcdfghjklmnpqrstvwxyz":
        con+=1
    else:
        continue
print(count)        
print(con)'''

'''count=0
con=0
inp="nAvya"
a,b="",""
inp=inp.lower()
for i in inp:
    if(i in "aeiou"):
        count+=1
        a=a+i
    elif i in "bcdfghjklmnpqrstvwxyz":
        con+=1
        b=b+i     
    else:
        continue
print(count)        
print(con)
print(a+b)'''





            


