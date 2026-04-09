from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(
        self, 
        numCourses: int, 
        prerequisites: List[List[int]], 
        queries: List[List[int]]
    ) -> List[bool]:
        
        # Step 1: Build graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        # Step 2: Store prerequisites of each node
        prereq = [set() for _ in range(numCourses)]
        
        # Step 3: Start with nodes having indegree 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # Step 4: Topological sort
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                # Add direct prerequisite
                prereq[neighbor].add(node)
                
                # Add all indirect prerequisites
                prereq[neighbor].update(prereq[node])
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 5: Answer queries
        return [u in prereq[v] for u, v in queries]