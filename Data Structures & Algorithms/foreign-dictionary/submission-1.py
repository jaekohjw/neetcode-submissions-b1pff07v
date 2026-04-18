class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for word in words for c in word}

        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    adj[c1].append(c2)
                    break

        state = {}  # 1 = visiting, 2 = visited
        res = []

        def dfs(c):
            if c in state:
                return state[c] == 2  # 2=done(True), 1=cycle(False)
            state[c] = 1
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            state[c] = 2
            res.append(c)
            return True

        for c in adj:
            if c not in state:
                if not dfs(c):
                    return ""

        return "".join(reversed(res))