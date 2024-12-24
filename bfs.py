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





graph={

"A":["B","C"],
"B" :["A","D","E"],
"C":["A","F"],
"D":["B"],
"E":["B","F"],
"F":["C"]


}
v=[]
q=[]

bfs(graph,v,"A",q)