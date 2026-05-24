class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        
        pointer=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for e in even:
            nums[pointer]=e
            pointer+=1
        for o in odd:
            nums[pointer]=o
            pointer+=1
        return nums
        