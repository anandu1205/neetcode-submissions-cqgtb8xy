class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST,mapTS={},{}
        n=len(s)
        for i in range(n):
            
                char_s=s[i]
                char_t=t[i]
                
                if char_s in mapST:
                    if mapST[char_s]!=char_t:
                      return False
                else:
                    mapST[char_s]=char_t

                if char_t in mapTS:
                     if mapTS[char_t]!=char_s:
                       return False
                else:
                    
                     mapTS[char_t]=char_s
        return True
        