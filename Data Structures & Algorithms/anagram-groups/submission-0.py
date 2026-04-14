class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        grps = 0
        res = []
        for s in strs:
            chars = {}
            for c in s:
                chars[c] = chars.get(c, 0) + 1
            if chars in anagrams:
                res[anagrams.index(chars)].append(s)
            else:
                anagrams.append(chars)
                res.append([s])
                grps += 1
        return res
            
        