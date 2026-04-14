class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        res = []
        most_freq = 0
        most_freq_k = 0
        for i in range(k):
            for k, v in counts.items():
                if v > most_freq:
                    most_freq = v
                    most_freq_k = k
            res.append(most_freq_k)
            del counts[most_freq_k]
            most_freq = 0
        
        return res