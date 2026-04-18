class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = [[] for _ in range(26)]
        chars = set()

        def toAscii(c):
            return ord(c) - ord("a")

        for word in words:
            for ch in word:
                chars.add(ch)
        

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            j = 0
            while j < min(len(word1), len(word2)) and word1[j] == word2[j]:
                j += 1

            if j < min(len(word1), len(word2)):
                adj_list[toAscii(word1[j])].append(toAscii(word2[j]))

        state = [0] * 26
        res = []

        def dfs(i):
            if state[i] == 1:
                return False
            if state[i] == 2:
                return True 
            
            state[i] = 1

            for nei in adj_list[i]:
                if not dfs(nei):
                    return False

            state[i] = 2
            res.append(chr(i + ord("a")))
            return True

        for c in chars:
            if state[toAscii(c)] == 0:
                if not dfs(toAscii(c)):
                    return ""

        return "".join(res)[::-1]