# #list order index allow duplicate
# # students = ["Alice", "Peter", "Diane", "Eric","Kevin"]
# # marks = [78, 45, 89, 32,67]
# # maxi = marks.index(max(marks))
# # print (students[maxi])

# # numbers  = (1,2,3,4,5,6,7,8,9)
# # num = (1,2,3)
# # age , years , times =num
# # print(age)
# # record = ("Alice", 19, 87)
# # name, age, mark = record
# # print(f"{name}")

# # student = ("RP026", "Alice", 78, 85, 92)
# # print (student[0])

# # student = {
# #     "rp":{"name" : "rty","age" : 12},
# #     "ur":{
# #         "name" : "cvbn",
# #         "age" : 66
# #     }
# # }
# # student["cur"] = {'name':'yhd','age':66}
# # print(student["cur"]["age"])
# # print()

# # def calculate_fee(course, fee):
# #     print("Course:", course)
# #     print("Fee:", fee)

# # calculate_fee("Python")
# # calculate_fee("AI", 75000)

# # def show_data(*args, **kwargs):
# #     print("Positional:", args)
# #     print("Keyword:", kwargs)

# # show_data(10, 20, name="Alice", course="Python")


# # def add_numbers(a, b):
# #     return a + b
# # #result = add_numbers(2,8)
# # print(add_numbers(2,8)*2)
# # #print(result * 2)

# # def calculate_marks(a, b, c):
# #     total = a + b + c
# #     average = total / 3
# #     return total, average

# # total_marks, average_marks = calculate_marks(70, 80, 90)

# # print("Total:", total_marks)
# # print("Average:", average_marks)


# # def factorial(n):
# #     if n < 0:
# #         raise ValueError("Factorial is not defined for negative integers")

# #     if n == 0 or n== 1:
# #         return 1

# #     return n * factorial(n - 1)

# # print(factorial(0))
# # print(factorial(5))

# # def myfunc(*long,**short):
# #     print("Total long : ",sum(long))
# #     for x,y in short.items():
# #      print("key : ",x ," \n vaue : ",y)
# # myfunc(1,2,name='yhd',age=45)

# # def student_report(name, marks):
# #     average = sum(marks)/ len(marks)
    
# #     if average >=50:
# #         print(name , "Pass")
# #     else:
# #         print(name,"Fail")
# #     return average

# # average1 = student_report("yhd",[70, 80, 90])
# # print(average1)


# # def student_report(student):
# #     average = sum(student['marks'])/ len(student['marks'])
    
# #     if average >=50:
# #         print(student['name'] , "Pass")
# #     else:
# #         print(student['name'],"Fail")
# #     return average

# # print(student_report(student = {'name':'yhd','marks':[70, 85, 95]}))

# # class Student:
# #     def __init__(self, name, marks):
# #         self.name = name
# #         self.marks = marks

# # student1 = Student("Peter", 60)

# # print(student1.marks)

# # student1.marks = 90

# # print(student1.marks)

# # class Student:
# #     def __init__(self, name, age, marks):
# #         self.name = name
# #         self.age = age
# #         self.marks = marks

# #     def calculate_average(self):
# #         if len(self.marks) == 0:
# #             return 0

# #         return sum(self.marks) / len(self.marks)

# #     def display_report(self):
# #         average = self.calculate_average()

# #         print("Student name:", self.name)
# #         print("Age:", self.age)
# #         print("Average marks:", average)

# #         if average >= 50:
# #             print("Result: Pass")
# #         else:
# #             print("Result: Fail")


# # student1 = Student("Peter", 20, [70, 80, 90])
# # student2 = Student("John", 21, [40, 45, 35])

# # student1.display_report()
# # print("----------------")
# # student2.display_report()

# class Student:
#   def __init__(self,name,marks):
#      self.name=name
#      self.marks=marks
#   def average_calc(self):
#      average = sum(self.marks) / len(self.marks)
#      return average
#   def report(self):
#      x = self.average_calc()
#      if x >=50:
#        print(self.name ,"Pass")
#      else:
#        print(self.name ,"Fail")
# stu1 = Student("Peter",[2,0,40])
# stu2 = Student("John",[33,20,40])
# print(stu2.average_calc())
# stu2.report()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print("My name is", self.name)
#         print("I am", self.age, "years old.")


# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         # self.name = name
#         # self.age = age
#         self.student_id = student_id

#     def study(self):
#         print(self.name, "is studying Python.")


# student1 = Student("Peter", 20, "RP026")

# student1.introduce()
# student1.study()
# print("Student ID:", student1.student_id)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class student(person):
    def __init__(self, name, age,regno):
        super().__init__(name, age)
        self.regno = regno
    def printi(self):
        print("Hello My Name Is ",self.name,"I'm ",self.age," Old with RegNo",self.regno)

st1 = student("yhd",34,'24RP03')
st1.printi()
