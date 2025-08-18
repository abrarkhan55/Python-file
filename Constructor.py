class Student():
    roll=""
    gpa=""

    def __init__ (self,roll,gpa):
     self.roll=roll
     self.gpa=gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

abrar=Student(10,3.50)
abrar.display()

nirob=Student(4,1.5)
nirob.display()