class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) - 1
        count = 0
        
        while l >= 0:
            if s[l] != ' ':
                count += 1
            elif count > 0:
                return count
            l -= 1
        
        return count