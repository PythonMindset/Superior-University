#DFS (Depth First Search) implentation for Tree

tree = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':[],
    '8':[],
}
visited=list()
def dfs(graph,node,goal):
    if (node not in visited) and (goal not in visited):
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,goal)
print("Depth First Search: ")
dfs(tree,'5','2')
print(visited)