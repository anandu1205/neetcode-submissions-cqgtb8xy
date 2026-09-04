class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            current_weight=0
            days_needed=1
            for i in range(0,n):
                if current_weight+weights[i]>mid:
                    days_needed+=1
                    current_weight=weights[i]
                else:
                    current_weight+=weights[i]
            
            if days_needed<=days:
                right=mid-1
            else:
                left=mid+1
        return left


        