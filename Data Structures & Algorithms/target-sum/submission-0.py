class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)

        if target > offset or target < -offset:
            return 0

        dp = [[0] * (2 * offset + 1) for _ in range(len(nums) + 1)]

        dp[0][offset] = 1

        for i in range(1, len(nums) + 1):
            for j in range(-offset, offset + 1):

                if -offset <= j - nums[i - 1] <= offset:
                    dp[i][j + offset] += dp[i - 1][j - nums[i - 1] + offset]

                if -offset <= j + nums[i - 1] <= offset:
                    dp[i][j + offset] += dp[i - 1][j + nums[i - 1] + offset]

        return dp[len(nums)][target + offset]