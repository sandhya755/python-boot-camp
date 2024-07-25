#multi level inheritance
class Father:
    def father_speak():
        return "Father class"
class Mother:
    def mother_speak():
        return "Mother class"
class Kid(Father,Mother):
    def kid_speak():
        return "i 'm Kid. i'm having a propreties"

obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())

'''
Father class
Mother class
i 'm Kid. i'm having a propreties
'''