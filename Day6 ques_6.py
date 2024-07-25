#multipul inheritance
class Animal:
    def speak():
        return "Animal is speaking"
    #single inheritance
class dog(Animal):
    def bark():
      return "Bow"
class puppy(dog):
     def shout():
       return "iam child"
     
obj1=Animal
obj2=dog
obj3=puppy
print(obj1.speak())
print(obj2.bark())
print(obj3.shout())
'''olp
Animal is speaking
Bow
iam child
'''