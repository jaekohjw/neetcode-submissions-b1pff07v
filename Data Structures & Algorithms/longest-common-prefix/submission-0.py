class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        max_length = len(min(strs))
        i = 0

        while i < max_length:
            ch = strs[0][i]
            for s in strs[1:]:
                if s[i] != ch:
                    return res
            res += ch
            i += 1

        return res


        