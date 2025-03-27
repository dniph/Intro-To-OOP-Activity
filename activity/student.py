class Student:
    def __init__(self, name, year, classes):
        self.name = name 
        self.year = year
        self.classes = classes

    def add_class(self, new_class):
        self.classes.append(new_class)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        num_courses = self.get_num_classes()
        print(f"{self.name} is a {self.year} enrolled in {num_courses} classes")



student_1 = Student("Samara", "junior", ["Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition"])
student_2 = Student("Claire", "freshman", ["Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science"])

student_1.add_class("Painting")
student_1.get_num_classes()
student_1.summary()

student_2.add_class(("Painting"))
student_2.get_num_classes()
student_2.summary()