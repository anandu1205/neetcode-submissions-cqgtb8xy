class Solution:
    def longestPalindrome(self, s: str) -> str:

        resIdx = 0
        resLen = 0
        n = len(s)

        for i in range(n):

            # odd length palindrome
            l = i
            r = i

            while l >= 0 and r < n and s[l] == s[r]:

                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1

                l -= 1
                r += 1

            # even length palindrome
            l = i
            r = i + 1

            while l >= 0 and r < n and s[l] == s[r]:

                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1

                l -= 1
                r += 1

        return s[resIdx:resIdx + resLen]




