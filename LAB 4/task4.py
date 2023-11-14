file = open('input4.txt','r')
result = open('output4.txt','w')


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


cylic = False
color = ['white']*(vertices+1)
def DFS(S):
    global cylic
    if color[S] == "white":
        print(S,end=' ')
        color[S] = "grey"
         
        for v in range(len(adj_list[S])):
            if adj_list[S][v] !=None and color[adj_list[S][v]] == "grey":
                cylic = True

            if adj_list[S][v] !=None and color[adj_list[S][v]] == "white":
             
                DFS(adj_list[S][v])
        color[S] = 'black'
DFS(1)

if cylic:
    result.write("YES")
else:
    result.write("NO")


'''
Explanation:
Here we modified the DFS a bit. We use color. white means a node is not visited. grey means visited but not fully explored,
black means node is fully explored. 
we taken a global variable name cyclic. Then we checked if we visit a grey node that means there is a cycle. made
cylic variable True. 
'''
    