class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        p=0
        while not l>=len(nums):
            if nums[l]==0:
                l+=1
            else:
                nums[p]=nums[l]
                p+=1
                l+=1
        while p<len(nums):
            nums[p]=0
            p+=1
            
                
            