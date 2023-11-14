
from queue_ import Queue


q = Queue()
file = open('input2.txt','r')
result = open('output2.txt','w')


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

def BFS(firs_vrtx):

    result.write(f"{firs_vrtx} ")
    visited[firs_vrtx] = 1 
    q.enqueue(firs_vrtx)

    while not q.isEmpty():
        u = q.dequeue()
        for v in range(len(adj_list[u])):
           
            if adj_list[u][v] !=None and visited[adj_list[u][v]] == 0:
                
                result.write(f"{adj_list[u][v]} ")
                visited[adj_list[u][v]] = 1 
                q.enqueue(adj_list[u][v])


BFS(1)


file.close()

'''
Explanation:

Here we used BFS Algorithm. we use a queue. We Start from the Source. After expolring all the child of that source we enqueue the childs
and marked them as visited. Then we deqeueue the queue and expolore its childs and marked as visited. These procedure
repeats untill the queue is empty. 
'''