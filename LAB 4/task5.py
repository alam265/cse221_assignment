from queue_ import Queue
import numpy as np


q = Queue()
file = open('input5.txt','r')
result = open('output5.txt','w')


graph_info = file.readline().split(' ')
vertices = int(graph_info[0])
edges = int(graph_info[1])
destination = int(graph_info[2])



matrix = np.zeros((vertices+1,vertices+1),dtype=int)


for i in range(edges):
    row,col= file.readline().split(' ')
    row = int(row)
    col = int(col)
    
    matrix[row][col] = 1
    matrix[col][row] = 1



visited = [0]*(vertices+1)
parent = [0]*(vertices+1)
distance = [0]*(vertices+1)

def BFS(firs_vrtx):
    global distance 

    
    visited[firs_vrtx] = 1 
    distance[firs_vrtx] = 0
    q.enqueue(firs_vrtx)

    while not q.isEmpty():
        u = q.dequeue()
        for v in range(1,vertices+1):         
            if matrix[u][v] ==1 and visited[v] == 0:
                
                
                visited[v] = 1 
                parent[v] = u
                distance[v] = distance[u]+1
                
                q.enqueue(v)


BFS(1)




result.write(f"Time: {distance[destination]}\n")



path = []
while destination!=0:
    path.append(destination)
    destination = parent[destination]

path =path[::-1]
result.write("Shortest Path: ")
for i in path:
    result.write(f"{i} ")




file.close()

'''
Explanation:
We made a slight modifiaction in BFS. we kept two array name parent and distance. 
Each time it visited a node these two variable kept the track of distance and parent. 

Lastly, we loop through the parent array from destination. basically, we did backtrack to find out the shortest
path
'''


