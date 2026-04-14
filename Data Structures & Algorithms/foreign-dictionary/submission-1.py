class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        unique_chars = set()
        
        # Step 1: collect all unique characters
        for word in words:
            unique_chars.update(word)
        
        # Step 2: initialize indegree
        in_degree = {c: 0 for c in unique_chars}
        
        # Step 3: build graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # prefix check
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break
        
        # Step 4: Kahn's algorithm
        queue = deque([c for c in unique_chars if in_degree[c] == 0])
        result = ""
        
        while queue:
            char = queue.popleft()
            result += char
            
            for nei in graph[char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        # Step 5: cycle check
        if len(result) != len(unique_chars):
            return ""
        
        return result
        