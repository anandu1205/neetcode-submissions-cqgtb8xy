class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        list1=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    list1.append(words[i])
                    break
        return list1


        