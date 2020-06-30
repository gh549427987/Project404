# coding: utf-8
# @Time    : 2020/6/23 8:00 下午
# @Author  : 蟹蟹 ！！
# @FileName: p06_继承与派生.py
# @Software: PyCharm

class people:

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school


class teacher(people):
    def __init__(self, name, age, school):
        super().__init__(name, age,school)

class student(people):
    def __init__(self, name, age, school):
        people.__init__(self, name, age, school)

print(teacher.mro())
obj = teacher()
print(obj.test())