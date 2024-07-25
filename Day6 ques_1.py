#we can give many classes in this method last in print what we given in a print satatement only  that will print
class Animal:
    def speak():
        return "Animal is speaking"
    #single inheritance
class dog(Animal):
    def bow():
      return "Bow"
class puppy(dog):
     def shout():
       return "iam child"
obj3=puppy
print(obj3.shout())

#o/p
#iam child