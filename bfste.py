#function for bfs
def bfs(graph,visit,node,queue):
    visit.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m,end=" ")

        for nodes in graph[m]:
            if nodes not in visit:
                visit.append(nodes)
                queue.append(nodes)

#function to construct

def build_graph(pairs):
    graph={}
    for u,v in pairs:
        if u not in graph:
            graph[u]=[]
        if v not in graph:
            graph[v]=[]
        graph[u].append(v)
        graph[v].append(v)
    return graph


n=int(input("Enter the number the pair you want:"))

pairs=[]
print("Enter {} pairs of edges:".format(n))

for _ in range(n):
    u,v=map(int,input().split())
    pairs.append((u,v))

# build graph
graph=build_graph(pairs)

#variable for bfs

v=[]
q=[]

#start node
no_de=int(input("ENter the start node:"))
bfs(graph,v,no_de,q)

