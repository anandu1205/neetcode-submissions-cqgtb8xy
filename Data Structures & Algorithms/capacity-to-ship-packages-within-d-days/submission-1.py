class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            current_weight=0
            days_required=1
            for weight in weights:
                if current_weight+weight>mid:
                    days_required+=1
                    current_weight=weight
                else:
                    current_weight+=weight
            if days_required<=days:
                right=mid-1
            if days_required>days:
                left=mid+1
        return left

        