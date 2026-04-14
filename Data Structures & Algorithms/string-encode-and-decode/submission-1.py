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
            i = j + 1
            j = i + length
            ret.append(s[i:j])
            i = j
        return ret
                
