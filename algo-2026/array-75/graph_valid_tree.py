from typing import List
def validTree(n: int, edges: List[List[int]]) -> bool:
    def build_graph(edges):
        graph = {node : [] for node in range(n)}
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        return graph
    graph = build_graph(edges)
    
    visited = set()
    def dfs(n, parent):
        for edge in graph[n]:
            if edge == parent:
                continue
            if edge in visited:
                return False
            visited.add(edge)
            if not dfs(edge, n):
                return False
        return True
    visited.add(0)
    acyclic = dfs(0, None)
    if not acyclic or len(visited) != n:
        return False
    else:
        return True
    