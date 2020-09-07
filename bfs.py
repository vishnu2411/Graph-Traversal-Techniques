n=int(input("Enter Number of Edges in the Graph\n"))
graph={}
for i in range(n):
    v=input("Enter the vertice\n")
    print("Enter the Neighbours of",v)
    neighbours=[]
    neighbours=list(map(str,input().split()))
    graph.update({v:neighbours})
   
print("\n\nThe Graph is:")
print(graph)

visited=[]
print("\nBFS Traversal is :")
visited=[]
q=[]
def bfs(graph,start):
    visited.append(start)
    q.append(start)
    print("\nThe BFS Path is:\n")
    while q:
        vertex=q.pop(0)
        print(vertex, end=" ")
        
        for adjacent in graph[vertex]:
            if adjacent not in visited:
                visited.append(adjacent)
                q.append(adjacent)

bfs(graph,'A')


