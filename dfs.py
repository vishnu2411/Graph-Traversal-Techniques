n=int(input("Enter Number of Edges in the Graph\n"))
graph={}
for i in range(n):
    v=input("Enter the vertice \n")
    print("Enter the Neighbours of",v)
    neighbours=[]
    neighbours=list(map(str,input().split()))
    graph.update({v:neighbours})
   
print("\n\nThe Graph is:")
print(graph)

visited=[]
print("\nDFS Traversal is :")
def dfs(graph,start):
    if start not in visited:
        print(start,end=" ")
        visited.append(start)
        for adjacent in graph[start]:
            dfs(graph,adjacent)

dfs(graph,'A')


