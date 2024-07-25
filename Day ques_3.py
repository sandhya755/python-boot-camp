#single inheritance
class Animal:
    def speak():
        return "Animal is speaking"
    #single inheritance
class dog(Animal):
    def bark():
      return "Bow"
obj1=Animal
print(obj1.speak())
'''
Animal is speaking
'''
