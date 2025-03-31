# add your get_student_with_more_classes function here!

def get_student_with_more_classes(student1, student2):
    
    if len(student1.classes) > len(student2.classes):
        return student1
    else:
        return student2