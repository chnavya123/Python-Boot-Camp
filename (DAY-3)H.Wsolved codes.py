#find even or odd
'''n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")'''    

#find greatest of 3
'''my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)''' 

#find the sum of all the elements in an array
'''arr=(5,3,2,4)
sum_of_elements=sum(arr)
print("the sum of elements in arr:",sum_of_elements)'''
            #(or)

'''arr=(2,4,5,6)
sum=0
for i in arr:
    sum+=i
print("the sum of elements is:",sum)'''    

#find peak element in an array
'''def find_peak_element(arr):
    n=len(arr)
    if n==0:
        return None
    if n==1:
       return arr[0]
    if arr[0]>=arr[1]:
        return arr[0]
    if arr[n-1]>=arr[n-2]:
        return arr[n-1]
    for i in range(1,n-1):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            return arr[i]
arr=[2,6,90,5,3]
peak=find_peak_element(arr)
print("peak element is:",peak)'''        
        
#find max element in an array
'''my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
print(max)'''

#find second max element in an array
'''my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
if len(my_list) < 2:
    print("Array must have at least two elements.")
else:
    max1 = None
    max2 = None
    for num in my_list:
        if max1 is None or num > max1:
            max2 = max1
            max1 = num
        elif num != max1 and (max2 is None or num > max2):
            max2 = num
    if max2 is None:
        print("No second maximum element found.")
    else:
        print("The second maximum element is:", max2)'''


#reverse of an array without using builtin fuctions
'''l=[2,8,9,5,6,7]
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")'''


#find the sum of squares of given number
'''n = int(input("Enter a number: "))
sum_squares = 0
for i in range(1, n + 1):
    sum_squares += i ** 2
print("The sum of squares of numbers from 1 to", n, "is:", sum_squares)'''

#find sum of squares even and odd  digits(different)
'''n = input("Enter a number: ")
sum_squares_even_digits = 0
for digit in n:
    digit_int = int(digit)  
    if digit_int % 2 == 0:  
        sum_squares_even_digits += digit_int ** 2  
print("The sum of squares of even digits is:", sum_squares_even_digits)'''


#check given number is palindrome or not using while loop
'''number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number = number // 10
if original_number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")'''

#write a program to print first n fibanocci series
'''n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b'''
