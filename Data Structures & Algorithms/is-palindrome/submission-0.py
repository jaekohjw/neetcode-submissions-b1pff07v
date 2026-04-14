class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            left = s[i]
            right = s[j]
            if not left.isalnum():
                i += 1
            elif not right.isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else: 
                return False
        return True
        