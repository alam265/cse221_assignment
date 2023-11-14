file = open('input1_B.txt','r')
result = open('output1_B.txt','w')


graph_info = file.readline().split(' ')
vertices = int(graph_info[0])
edges = int(graph_info[1])

adj_list = []
for i in range(vertices+1):
    adj_list.append([])


for i in range(edges):
    source,destination,weight = file.readline().split(' ')
    source = int(source)
    destination =int(destination)
    weight = int(weight)

    adj_list[source].append((destination,weight))





for i in range(len(adj_list)):
    if adj_list[i] ==[]:
        result.write(f"{i}: ")
        result.write(f"\n")
    else:
        result.write(f"{i}: ")
        for j in range(len(adj_list[i])):
            result.write(f"{adj_list[i][j]} ")
        result.write(f"\n")

    '''
    Explanation:
    Here we created a list. Then we created some list based on how many vertices we have. After that we append all
    those list inside a list that we created first. Thus, we create a adjacency list using Nested list. Finally, we 
    represented the graph. 
    '''    
