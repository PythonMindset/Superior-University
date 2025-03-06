graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["F"],
    "F":[]
}
def dfs(graph,start):
    stack=[start]
    visited=[]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            print(node)
            for i in graph[node]:
                stack.append(i)
dfs(graph,"D")
