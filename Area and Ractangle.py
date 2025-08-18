class shape:
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2

    def area(shape):
        print("This is area part ")

class triangle(shape):
    def area(self):
        area=0.5* self.c1* self.c2
        print("This is triangle part ",area)


class ractangle(shape):
    def area(self):
        ractangle= self.c1* self.c2
        print("This is Ractangle part",ractangle)

t1= triangle(50,60)
t1.area()
r1=ractangle(50,60)
r1.area()