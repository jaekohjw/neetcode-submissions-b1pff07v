class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if length > len(s2):
            return False
        
        dict1 = {}
        for c in s1:
            dict1[c] = 1 + dict1.get(c, 0)

        for i in range(0, len(s2) - length + 1):
            dict2 = {}
            for j in range(i, i + length):
                dict2[s2[j]] = 1 + dict2.get(s2[j], 0)
                if dict1.get(s2[j], 0) < dict2[s2[j]]:
                    break
            if dict1 == dict2:
                return True 

        return False