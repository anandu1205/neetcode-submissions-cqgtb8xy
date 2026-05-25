class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        boat=0
        while left<=right:
            rem=limit-people[right]
            boat+=1
            right-=1
            if rem>=people[left]:
                left+=1
        return boat
