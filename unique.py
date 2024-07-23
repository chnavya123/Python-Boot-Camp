#print unique letters in a string
'''vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)'''

   

vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
e="hello 123 world"
inp=e.lower()
for i in e:
    if(i in check):
        ans+=int(i)
print(ans)

#reverse the numbers present in the given string
'''n=input("enter string: ")
rev_str=""
for i in n:
     rev_str=i+rev_str
print("reverse of the given string",rev_str)
if n==rev_str:
    print("is a palindrome")
else:
    print("is not a palindrome")'''
