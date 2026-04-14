class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = 1 
        max_length = 1;
        mySet = {s[l]}

        while r < len(s):
            new_char = s[r]
            if new_char not in mySet:
                mySet.add(new_char)
                max_length = max(max_length, r - l + 1)
            else:
                while new_char in mySet:
                    mySet.remove(s[l])
                    l += 1;
                mySet.add(new_char)
        
            r += 1;

        return max_length;







        