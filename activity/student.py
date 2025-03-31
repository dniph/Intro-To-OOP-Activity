class Student:
    def __init__(self, name, year, classes):
        self.name = name 
        self.year = year
        self.classes = classes
        
    def add_class(self,new_class):
        self.classes.append(new_class)
        return self.classes
        

        
    
        
    