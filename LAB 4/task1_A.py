import numpy as np 

file = open('input1_A.txt','r')
result = open('output1_A.txt','w')


graph_info = file.readline().split(' ')
vertices = int(graph_info[0])
edges = int(graph_info[1])

matrix = np.zeros((vertices+1,vertices+1),dtype=int)


for i in range(edges):
    row,col,weight = file.readline().split(' ')
    row = int(row)
    col = int(col)
    weight = int(weight)

    matrix[row][col] = weight 


for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        result.write(f"{matrix[row][col]} ")
    result.write('\n')


'''
Explanation:
We created a 2D array using numpy. Then we populated the array using a loop. Inside the loop we read each lines
and populated the array according to the info.
'''