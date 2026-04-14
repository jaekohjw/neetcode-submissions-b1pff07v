class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if len(s1) > len(s2):
            return False
        
        dict1 = {}
        for i in range(len(s1)):
            dict1[s1[i]] = 1 + dict1.get(s1[i], 0)

        for i in range(0, len(s2) - length + 1):
            dict2 = {}
            for j in range(i, i + length):
                dict2[s2[j]] = 1 + dict2.get(s2[j], 0)
            if dict1 == dict2:
                return True 

        return False