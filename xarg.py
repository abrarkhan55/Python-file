#xarg
'''def add(*abrar):
    sum=0
    for i in abrar:
        sum=sum+i
    print(sum)

add(10,20,30)
add(11,22,33,44)
add(111,222,333,444,555)'''

#xxarg
def add(**details): #xxarg mainly ** diye used hoi
    print(details["mobile"]) #then print korte hbe chaile index or nicher cgpa roll ai gulo o dekha jabe ["cgpa"] amn vabe

add(id=100,name="Abrar",cgpa=4.00,roll=24,basha="pabna",mobile="0123") #aikhane must be id= ai gulo veriable used korte hbe

