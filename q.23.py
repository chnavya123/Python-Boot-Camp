#LCM of two numbers
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=a*b
while b!=0:
    a,b=b,a%b
    print("gcd of two numbers:",a)
lcm=c//a
print("lcm of two numbers:",lcm)


    
    

