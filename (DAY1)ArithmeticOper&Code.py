'''a=int(input())
b=int(input())
print(a+b,a-b)
print(a**b)'''

'''    
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a**b)
print(a//b)
'''

'''
age=int(input())
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>24 and age<45):
    print("two wheelers and four wheelers")
else:
    print("All")  ''' 
    
'''
apple=int(input())
bananas=int(input())
oranges=int(input())
total=700
sum=apple*15+bananas*12*4+oranges*5
if(sum<=total):
    print(" not cheated")
else:
    print(' cheated')
'''

'''
#even and odd numbers
n=int(input())
if(n%2==0 and n>0):
    print("even positive number")
elif(n%2==0 and 0>n):
    print("even negative number")
elif(n%2!=0 and 0<n):
    print("odd positive number")
else:
    print("odd negative number")
'''


'''mr.z is selected for olympics,he is participating in swimming competition.Only one winner is selected in all the participants.mr.x and mr.y are frnds of z.
mr.x is participating in badmiton and mr.y in table tennis,according to the selection committee,the requirements for the badminton players are 140 cm height,
weight:factors of 2,body fat<12%.according to the selection committee,requirements of table tennis are
                                      height:min 118cm-148cm,weight:factors of no. of medals won by mr.z,bodyfat:14%
               according to the previous history z participated in 14 games out of which he is having success rate of 65%.Write a program 
     mr.x and mr.y and mr.z from india travel in a same plane or not?       '''

# Example data
mr_x_height = 150  # Example height for Mr. X in cm
mr_x_weight = 70   # Example weight for Mr. X in kg

mr_y_height = 130  # Example height for Mr. Y in cm
mr_y_weight = 3    # Example weight for Mr. Y in kg (number of medals factor)

mr_z_games = 14        # Total games Mr. Z participated in
mr_z_success_rate = 65  # Success rate of Mr. Z

# Calculate Mr. Z's number of medals
mr_z_medals = round(mr_z_games * (mr_z_success_rate / 100))

# Check Mr. X's selection criteria for Badminton
if mr_x_height >= 140:
    if mr_x_weight % 2 == 0:
        mr_x_selected = True
    else:
        mr_x_selected = False
else:
    mr_x_selected = False

# Check Mr. Y's selection criteria for Table Tennis
if 118 <= mr_y_height <= 148:
    if mr_y_weight % mr_z_medals == 0:
        mr_y_selected = True
    else:
        mr_y_selected = False
else:
    mr_y_selected = False

# Check if Mr. X and Mr. Y will travel with Mr. Z
if mr_x_selected and mr_y_selected:
    print("Mr. X and Mr. Y will travel with Mr. Z to the Olympics.")
else:
    print("Mr. X and Mr. Y will not travel with Mr. Z to the Olympics.")
