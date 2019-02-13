####################
# USING CLASSES
####################


class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(self.name, self.age, self.gender)
    
    def getDetails(self):
        print()
        
    def changeName(self, newName):
        self.name = newName
        
    def tenperles(self, salary):
        self. newSalary = salary - (salary * 0.10)
        
if __name__ == "__main__":
    Milly = Person("Milly", 19, "Female")
    Milly.getDetails()
    Milly.changeName("Jade2")