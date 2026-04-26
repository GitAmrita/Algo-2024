
from typing import List

def connectedComponents(self, n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    joined = 0
    def find(e):
        if parent[e] != e:
            parent[e] = find(parent[e])
        return parent[e]
    
    for e1, e2 in edges:
        f1 = find(e1)
        f2 = find(e2)
        if f1 != f2: 
            joined += 1
            parent[f1] = f2
    return n - joined