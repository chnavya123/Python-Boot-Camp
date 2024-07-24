class Animal:
    def Speak():
        return "animal speak"
class Dog(Animal):    
    def Speak():
        return "dog is barking"
class Kitten(Dog):    
    def Speak():
        return "kitten eat"
obj3=Kitten
print(obj3.Speak())

#method overiding
#class Animal:
#    def speak():
#        return "animal is speaking"
#class dog(Animal):
#    def speak():
#        return "dog is speaking"
#class puppy(dog):
#    def speak():
#        return "puppy is speaking"
#obj3=puppy
#print(obj3.speak())