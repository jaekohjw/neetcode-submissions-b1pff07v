class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, max_cnt = k, 0
        window_cnt = Counter()
        l = r = 0

        for r in range(len(s)):
            c = s[r]
            window_cnt[c] += 1
            if window_cnt[c] > max_cnt:
                max_cnt = window_cnt[c]

            replace = r - l + 1 - max_cnt
            if replace > k:
                window_cnt[s[l]] -= 1
                l += 1 
        
            longest = max(longest, r - l + 1)
                

        return longest


            


        
        