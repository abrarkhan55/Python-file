# filter basic
num=[1,2,3,4,5]
result=list (filter(lambda x: x % 2 ==0,num ))
print(result)
#filter advance or comprehansive
num=[1,2,3,4,5]
resul=[x for x in num if x%2==0]
print(resul)