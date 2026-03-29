class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank={c:i for i,c in enumerate(order)}
        boolean_value=[]
        no_of_words=len(words)
        for i in range(0,no_of_words):
            if (i<=no_of_words) and (i+1)<=(no_of_words-1):
                word1, word2 = words[i], words[i+1]
                for j in range(min(len(word1), len(word2))):
                    if word1[j] != word2[j]:
                        if rank[word1[j]] > rank[word2[j]]:
                            return False
                        break
                else:
                    if len(word1) > len(word2):
                        return False
        return True