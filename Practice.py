#build in polymorphism
print(len("A"))
print(len([10,20,30]))

#user define polymorphism
def add (x,y,z=0):
    return x + y+z

print(add(2,3))
print(add(2,3,4))