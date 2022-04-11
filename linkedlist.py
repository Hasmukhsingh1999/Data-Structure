#class is a blueprints of objects
# attributes -> variables , Behaviour -> Methods
# self ->object which you're passing
# instance and class var are static var
# class Computer:
#     def __init__(self):
#         self.name = "Hasmukh"
#         self.age = 22
#     def update(self):
#         self.age = 20
#     def compare(self,other):
#         if self.age==other.age:
#             return True
#         else:
#             return False
#
# c1 = Computer()
# c1.age=41
# c2 = Computer()
#
# if c1.compare(c2):
#     print("They are same")
# else:
#     print("They are different")
#
# print(c1.name)
# print(c1.age)
# namespace is an area where you create and store object/variable
# class Car:
#     wheels=4 #class variables
#     def __init__(self):
#         self.mil=10
#         self.com="Porche"
#
# c1=Car()
# c2=Car()
# c1.mil=8
#
#
# print(c1.mil,c1.com,c1.wheels)
# print(c2.mil,c2.com,c1.wheels)

# ------------------------------------------------------ TYPES OF METHODS ------------------------------------------------------
# class Student:
#     school = 'Telusko'
#     def __init__(self,marks1,marks2,marks3):
#          self.marks1=marks1
#          self.marks2=marks2
#          self.marks3=marks3
#     def average(self):
#         return (self.marks1+self.marks2+self.marks3) // 3
#     # def get_m1(self):
#     #     return self.marks1
#     # def set_m1(self,values):
#     #     self.marks1=values
#     @classmethod
#     def get_school(cls):
#         print(cls.school)
#     def info():
#         print("This is student class.. in abc module")
#
#
# # 1st type accessor methods ---> " TO fetch the value of instances var we use accessor" get method
#
# # 2nd type mutator methods  --->  "To modify the value we use mutator set method
#
# s1 = Student(90,89,75)
# s2 = Student(100,76,89)
#
# print(s1.average())
# Student.info()
# print(Student.info())
#
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.Laptop()
#
#     def show(self):
#         print(self.name,self.rollno)
#
#     class Laptop:
#         def __init__(self):
#             self.brand = "Dell"
#             self.cpu = "R5"
#             self.ram = 8
#     def show_lap(self):
#         print(self.brand,self.cpu,self.ram)
#
#
# s1= Student("Hasmukh ",27)
# s2=Student("Jenny",28)
# s1.show()
#  --------------------------------------------- INHERITANCE-----------------------------------------
# class A:
#     def __init__(self):
#         print(" in  A init")
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")
# class B: # when you create object of sub class it will call init of sub class first
#     # super() is a super class which is use to call th einit method of the parent class
#     # def __init__(self):
#     #     super().__init__()
#     #     print(" in  B init")
#     def feature3(self):
#         print("Feature 3 working")
#     def feature4(self):
#         print("Feature 4 working")
# # when one class inheriting from other 2 classes keeping in mind that those 2 classes were independent eachother,
# # is called multiple inheritance
#
# class C(A,B):  #method resolution order
#     def __init__(self):
#         super().__init__()
#     def feature5(self):
#         super().feature2()
#         print(" in c ")


# a1=C()
# a1.feature1()
# a1.feature2()
# b1= B()
# b1.feature3()
# b1.feature4()
# c1=C()
# c1.feature1()

# ------------------------------------------POLYMORPHISM-------------------------------------
# class pycharm:
#
#     def execute(self):
#         print("Compiling")
#         print("running")
# class Myeditor:
#     def execute(self):
#         print("Spell")
#         print("Convention")
#         print("Comiplier")
#         print("Running")
# class laptop:
#     def code(self,ide):
#         ide.execute()
#
# ide=Myeditor()
# lap1=laptop()
# lap1.code(ide)



#class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = Non
def  product(fracs):
    p = Fraction(reduce(lambda a, b: a*b,fracs))
    return p.numerator,p.denominator

if __name__=="__main__":
    fracs= []
    n = int(input())
    for i in range(n):
        fracs.append(Fraction(*map(int,input().split())))
    res=product(fracs)
    print(*res)
