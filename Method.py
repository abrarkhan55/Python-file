class student():
    name=""
    roll=""
    gpa=""

    def setup(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa

    def display(self):
            print(f"Name:{self.name},Roll:{self.roll},GPA:{self.gpa}")
abrar=student()
abrar.setup("Abrar",24,3.50)
abrar.display()

mim=student()
mim.setup("Mim",25,3.45)
mim.display()