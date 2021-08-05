students_list = ["Natasha", "Luis", "Jorge", "Carlos"]
print(students_list)

"""
print(students_list[0])
print(students_list[1])
print(students_list[-1])
print(students_list[2])
print(students_list[3])
"""

#insert
students_list.insert(0, "Gerardo")
print(students_list)

#append
students_list.append("Renato")
print(students_list)

#remove
students_list.remove("Luis")
print(students_list)

#pop
students_list.pop(0)
print(students_list)
students_list.pop(1)
print(students_list)

#del
del students_list[0]
print(students_list)