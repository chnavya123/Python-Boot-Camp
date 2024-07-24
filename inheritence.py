#write a code to demonstrate single,multiple,andmulti-level inheritence   
#class Myclass:
#    def add(a,b):
#        return a+b
#    def sub(a,b):
#        return a-b
#    def mul(a,b):
#        return a*b
#    def div(a,b):
#        return a/b
#    def mod(a,b):
#        return a%b
#obj1=Myclass
#print(obj1.add(2,4))
#print(obj1.sub(2,4))
#print(obj1.mul(2,4))
#print(obj1.div(2,4))
#print(obj1.mod(2,4))

#inheritance
#class Animal:
#    def Speak():
#        return "Animal is speaking"
##single inh:
#class Dog(Animal):
#    def Bark():
#        return "bow..."
#class puppy(Dog):
#    def puppy_speak():
#        return "im puppy"
#obj1=Animal
#obj2=Dog
#obj3=puppy
#print(obj3.Speak())
#print(obj3.Bark())
#print(obj3.puppy_speak())

#multiple inh:
class Father:
    def Father_speak():
        return "father is speaking"
class Mother:
    def Mother_speak():
        return "mother is speaking"
class son:
    def son_speak():
        return "i acquire characters from father and mother"
obj3=son
print(obj3.son_speak())

