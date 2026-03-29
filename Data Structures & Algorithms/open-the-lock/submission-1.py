class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue=deque([("0000",0)])
        visited=set(["0000"])
        dead=set(deadends)
        while queue:
            node,steps=queue.popleft()
            if node==target:
                return steps
            for i in range(4):
                digit=int(node[i])
                for move in [-1,1]:
                    new_digit=(digit+move)%10
                    new_node=node[:i]+str(new_digit)+node[i+1:]
                    if new_node not in visited and  new_node not in dead:
                        visited.add(new_node)
                        queue.append((new_node,steps+1))
        return -1
        