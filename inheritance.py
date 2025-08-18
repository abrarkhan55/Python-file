class Mobile:
    def call(self):
        print("call please")
    def massage(self):
        print("massage please ")


class walton(Mobile): #Mobile ta uporer parents oi take subclass or child class diye disi ata key inheritance bole

    """def call(self):
        print("call please")"""

    def massage(self):
        print("massage please ")

"""m=Mobile()
m.call()
m.massage()"""

w=walton()
w.call()
w.massage()
print(issubclass(Mobile,walton)) #this is a not parent class this is child class that's way false
print(issubclass(walton,Mobile))#this is a parent class this isnot child class that's way true