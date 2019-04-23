"""
    From the code below create 3 students and add them to a list.
    sort the list based on the students age.
    Print out the Students names from the list (use a list comprehension for this)
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name: {self.name} age: {self.age}'


if __name__ == '__main__':
    list_of_students = [Student("Karl", 23), Student("Ib", 48), Student("Hans", 19)]

    sorted_list = sorted(list_of_students, key=lambda student: student.age)

    print(sorted_list)
