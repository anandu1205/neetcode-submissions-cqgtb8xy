class Solution:
    def isHappy(self, n: int) -> bool:
        def sum(n: int) -> int:
            output=0
            while n:
                digit=n%10
                output=output+(digit**2)
                n=n//10
            return output
        visited=set()
        
        while n not in visited:
            visited.add(n)
            if n==1:
                return True
            n=sum(n)
        return False 
        