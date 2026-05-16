class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(temp: str) -> bool:
            l = 0
            r = len(temp) - 1

            while l < r:
                if temp[l] == temp[r]:
                    l += 1
                    r -= 1
                else:
                    return False

            return True

        for i in range(len(s)):
            temp = s[:i] + s[i+1:]

            if palindrome(temp):
                return True

        return palindrome(s)
        