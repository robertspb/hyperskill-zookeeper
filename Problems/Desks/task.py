class1 = int(input())
class2 = int(input())
class3 = int(input())
students_per_desk = 2
desks_for_class1 = class1 // students_per_desk + class1 % students_per_desk
desks_for_class2 = class2 // students_per_desk + class2 % students_per_desk
desks_for_class3 = class3 // students_per_desk + class3 % students_per_desk
desks = desks_for_class1 + desks_for_class2 + desks_for_class3
print(desks)
