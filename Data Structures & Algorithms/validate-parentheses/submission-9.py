class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        pairs = {")": "(", "}": "{", "]": "["}

        for i in range(len(s)):
            elem = s[i]
            if elem not in pairs:
                brackets.append(elem)
            elif not brackets:
                return False
            elif pairs[elem] != brackets.pop():
                return False
        return not brackets
