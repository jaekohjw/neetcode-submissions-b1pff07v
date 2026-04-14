class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False
        
        debt = Counter(s1)

        for i in range(n1):
            debt[s2[i]] -= 1
        
        if all(v == 0 for v in debt.values()):
            return True

        for i in range(n1, n2):
            debt[s2[i]] -= 1
            debt[s2[i - n1]] += 1

            if all(v == 0 for v in debt.values()):
                return True
        
        return False