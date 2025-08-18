matrix=[
    [10,20,30,1,2],
    [20,21,32,4,6],
]
'''print(matrix [1] [2]) #normal matrix

matrix [1] [4]=200 that's mean 1 row ar 4 col ar man update korlam
print(matrix [1] [4])'''

for row in matrix: # using nested for loop
    for col in row:
        print(col)