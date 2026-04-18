from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Clean, one-line extraction of unique characters
        unique_chars = set("".join(words))
        
        # 2. Use sets for adjacency to prevent duplicate edges
        adj = {c: set() for c in unique_chars}
        in_degree = {c: 0 for c in unique_chars}


        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    # 3. Only update in_degree if we haven't seen this exact edge yet
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break

        q = deque([c for c in in_degree if in_degree[c] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in adj[c]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(in_degree) else ""