file=open("Abrar.txt","r")
#print(file.readable())
read=file.read()   #if i file read so that's way to apply
print(read)
size=len(read) #if i found out in file "size" that's way to apply
print(size)
"""
p=file.readlines() [2] #If i file read in specificline then apply to way
print(p)

for x in file :
    print(x)"""

file.close()