import numpy as np 

file = open('input3.txt','r')
result = open('output3.txt','w')


graph_info = file.readline().split(' ')
vertices = int(graph_info[0])
edges = int(graph_info[1])

adj_list = []
for i in range(vertices+1):
    adj_list.append([])


for i in range(edges):
    source,destination = file.readline().split(' ')
    source = int(source)
    destination =int(destination)
    

    adj_list[source].append(destination)



visited = [0]*(vertices+1)
def DFS(S):
    if visited[S] == 0:
        result.write(f"{S} ")
        visited[S] = 1 
        for v in range(len(adj_list[S])):
            if adj_list[S][v] !=None and visited[adj_list[S][v]] == 0:
                DFS(adj_list[S][v])
DFS(1)
'''
Explanation:
DFS algorithm is used here.It starts from the source and visit the all the nodes till the end of the path. then it
return to the previous node and cheked if there any other path exist or not. it exist it visite the path. Thus, the steps
were done recursevely. 


'''