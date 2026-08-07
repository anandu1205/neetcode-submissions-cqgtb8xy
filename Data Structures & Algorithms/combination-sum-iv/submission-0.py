class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # dp[i] = number of permutations that sum to i

        dp = [0] * (target + 1)

        # Base case
        dp[0] = 1

        # Build answers from smaller sums to larger sums
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]