from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            if dp[i] == False:
                continue

            for word in wordDict:
                length = len(word)

                if s[i:i + length] == word:
                    dp[i + length] = True

        return dp[n]