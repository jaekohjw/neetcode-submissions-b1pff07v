class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            res = ""
            length = int(s[i:j])
            for k in range(j + 1, j + 1 + length):
                res += s[k]
            ret.append(res)
            i = j + 1 + length
        return ret
                
