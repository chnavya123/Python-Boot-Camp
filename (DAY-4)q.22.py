#GCD of 2 numbers:
#Euclidean Algorithm:
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is:",a)
