#map basic
def squre(x):
    return x*x
num=[1,2,3,4,5]
result=list (map(squre,num))
print(result)

#map comprehansive or map ar sortcut updated version
numbers=[1,2,3,4,5,6,7,8,9,10]
l=[x*x for x in numbers]
print(l)


