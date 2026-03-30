from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Step 1: Build graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Step 2: Initialize queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        order = []

        # Step 3: BFS
        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # Step 4: Cycle check
        return order if len(order) == numCourses else []
        