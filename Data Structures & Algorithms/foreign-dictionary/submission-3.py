from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {}
        in_degree = {}
        count = 0

        for word in words:
            for c in word:
                if c not in adj:
                    count += 1
                    adj[c] = []
                    in_degree[c] = 0


        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    adj[c1].append(c2)
                    in_degree[c2] += 1
                    break

        q = deque([c for c in in_degree if in_degree[c] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)
            count -= 1

            for nei in adj[c]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return "".join(res) if count == 0 else ""