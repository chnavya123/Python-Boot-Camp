'''my_list=[1,2,3,4]
print(my_list)'''

'''my_list=[1,2,3,4]
print(*my_list)  '''

#=[1,2,3,4]
#my_list=[9,6,3,-2]
#my_list.append(9999)
#my_list.insert(0,2)
#print((my_list))

'''my_list.pop(2)
print(*my_list)'''

'''my_list_2=[5,6,7,8]
new_lst=my_list+my_list_2
print(*my_list)'''

#cnt=my_list.count(2)
#print(cnt)

#my_list.sort()
#print(*my_list)

#my_list=list(map(int,input().split(" ")))
#print(*my_list)

#my_list=list(map(int,input().split("@")))
#print(*my_list)

#my_list=list(map(str,input().split(" ")))
#print(*my_list)

'''my_list=list(map(int,input().split(" ")))
my_list.append(89)
cnt=my_list.count(2)
my_list.insert(0,1)
print(cnt)
print(*my_list)'''

'''take input from the user if-user enter 1
1-append a new element,2-pop
3-sort,4-print good morning or print len,good morning,len(str)'''


my_list=list(map(str,input().split(" ")))
choice = int(input("Select any option (1: append, 2: pop, 3: sort, 4: length): "))
if choice==1:
    my_list.append(5)
    print(my_list)
elif choice==2:
    my_list.pop(5)
    print(my_list)
elif choice==3:
    my_list.sort()
    print(my_list)
else:
    print("good morning"+" length of your list is: "+str(len(my_list))) 

'''my_list=list(map(int,input().split(" ")))
for i in range(len(my_list)):
    print(my_list[i],end=" ")'''

'''str='navya'
for i in range(len(str)):
    print(str[i],end=" ")'''

'''1.using for loop append 1 to 100 numbers in empty list
2.find sum of all the numbers in a list
3.using for loop print 1-100 . '''

'''numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)'''


'''numbers = list(range(1, 6))
total_sum_function = sum(numbers)
print("The sum of all numbers in the list using sum function is:", total_sum_function)
total_sum_loop = 0
for num in numbers:
    total_sum_loop += num
print("The sum of all numbers in the list using for loop is:", total_sum_loop)'''


'''for i in range(1, 101):
    print(i)'''


# Task 1: Append numbers 1 to 100 to an empty list using a for loop
'''numbers = []
for i in range(1, 101):
    numbers.append(i)'''

# Task 2: Find the sum of all the numbers in the list
'''numbers=[2,3]
total_sum = sum(numbers)
print("The sum of all numbers in the list is:", total_sum)'''

# Task 3: Print numbers 1 to 100 using a for loop
'''for i in range(1, 101):
    print(i)'''
