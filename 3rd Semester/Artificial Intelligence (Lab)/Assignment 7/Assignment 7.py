def task1():
    class AStar():
        def __init__(self,graph):
            self.graph=graph
        
        def neighbors(self,v):
            return self.graph[v]
        
        def heuristic(self,n):
            heuristic_values={
                "A":1,
                "B":1,
                "C":1,
                "D":1
            }
            return heuristic_values[n]

        def a_star(self,start,goal):
            open_list=[start]
            closed_list=[]
            g={}
            g[start]=0
            parents={}
            parents[start]=start
            while len(open_list)>0:
                n=open_list[0]
                for i in open_list:
                    if g[i]+self.heuristic(i)<g[n]+self.heuristic(n):
                        n=i
                if n==None:
                    print("Path does not exist!!")
                    return None
                if n==goal:
                    path=[]
                    while parents[n]!=n:
                        path.append(n)
                        n=parents[n]
                    path.reverse()
                    path.append(start)
                    print(f"Path found: {path}.")
                    return path
                open_list.remove(n)
                closed_list.append(n)
                for (m,weight) in self.neighbors(n):
                    if m not in open_list and m not in closed_list:
                        open_list.append(m)
                        parents[m]=n
                        g[m]=g[n]+weight
                    else:
                        if g[m]>g[n]+weight:
                            g[m]=g[n]+weight
                            parents[m]=n
                            if m in closed_list:
                                closed_list.remove(m)
                                open_list.append(m)
                open_list.remove(n)
                closed_list.append(n)
            print("Path does not exist!!")
            return None
    graph={
        "A":[("B",1),("C",3),("D",7)],
        "B":[("D",5)],
        "C":[("D",12)]
    }
    obj1=AStar(graph)
    obj1.a_star("A","D")
# task1()


def task1():
    class AStar:
        def __init__(self, graph):
            self.graph = graph
        
        def neighbors(self, v):
            return self.graph.get(v, [])  # Return empty list if node not found
        
        def heuristic(self, n):
            heuristic_values = {"A": 1, "B": 1, "C": 1, "D": 1}
            return heuristic_values.get(n, 0)  # Default heuristic is 0 if missing

        def a_star(self, start, goal):
            open_list = [start]  # Nodes to explore
            closed_list = []  # Explored nodes
            g = {start: 0}  # Cost from start node
            parents = {start: None}  # Stores path

            while open_list:
                # Pick the node with the lowest f(n) = g(n) + h(n)
                n = min(open_list, key=lambda x: g[x] + self.heuristic(x))

                if n == goal:  # If we reached the goal, reconstruct path
                    path = []
                    while n is not None:
                        path.append(n)
                        n = parents[n]
                    path.reverse()
                    print(f"Path found: {path}")
                    return path

                open_list.remove(n)
                closed_list.append(n)

                for (m, weight) in self.neighbors(n):
                    if m in closed_list:
                        continue  # Skip already explored nodes

                    new_g = g[n] + weight  # Calculate new cost

                    if m not in open_list or new_g < g.get(m, float('inf')):
                        g[m] = new_g
                        parents[m] = n
                        if m not in open_list:
                            open_list.append(m)

            print("Path does not exist!")
            return None

    graph = {
        "A": [("B", 1), ("C", 3), ("D", 7)],
        "B": [("D", 5)],
        "C": [("D", 2)],  # Reduced weight for a better path
        "D": []  # Added "D" to avoid key errors
    }
    
    obj1 = AStar(graph)
    obj1.a_star("A", "D")

task1()


