from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    @abstractmethod
    def area(shape):
        pass


class Triangle(shape):
    def area(self):

        Triangle=0.5* self.dim1* self.dim2
        print("This is area part ",Triangle)


class Ractangle(shape):
    def area(self):
        Ractangle=self.dim1* self.dim2
        print("This is Ractangle ",Ractangle)


t1=Triangle(20,30)
t1.area()

r1=Ractangle(30,40)
r1.area()