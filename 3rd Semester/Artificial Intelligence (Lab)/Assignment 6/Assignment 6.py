def task1():
    graph={
        "A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],
        "E":["F"],
        "F":[]
    }
    def bfs(graph, start):
        visited_nodes = []
        current_level = [start]
        
        while current_level:
            next_level = []
            for node in current_level:
                if node not in visited_nodes:
                    visited_nodes.append(node)
                    next_level.extend(graph[node])
            current_level = next_level
        print (visited_nodes)
    bfs(graph, "A")
# task1()

def task2():
    graph={
        "A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],
        "E":["F"],
        "F":[]
    }
    def bfs(graph,start):
        visited=[]
        queue=[start]
        while queue:
            current=queue.pop(0)
            print(current,end='')
            if current in graph:
                for i in graph[current]:
                    if i not in visited:
                        queue.append(i)
                        visited.append(i)
            print()
    bfs(graph,"A")
# task2()
