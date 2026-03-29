"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldtoNew = {}

        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]

            copy = Node(node.val)
            oldtoNew[node] = copy

            for nei in node.neighbors:   # fixed spelling
                copy.neighbors.append(dfs(nei))  # added dfs(nei)

            return copy

        return dfs(node)     