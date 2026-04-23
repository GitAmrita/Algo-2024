
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]                                                                                                
    for a, b in prerequisites:                                                                                                             
        graph[b].append(a)                                                                                                                 
                                                                                                                                            
    state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=done

    def dfs(node):                                                                                                                         
        if state[node] == 1:
            return False  # cycle found                                                                                                    
        if state[node] == 2:
            return True   # already processed

        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):                                                                                                          
                return False
        state[node] = 2                                                                                                                    
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


if __name__ == "__main__":
    canFinish(4, [[1, 0], [2, 1], [3, 2]])   # no cycle
    print() [[1,0]]
    canFinish(2, [[1, 0]])    # cycle
    print()        
