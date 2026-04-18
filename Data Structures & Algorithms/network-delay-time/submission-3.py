import heapq 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distances = [float('inf') for _ in range(n + 1)]
        distances[k] = 0

        for _ in range(n - 1):
            for u, v, t in times:
                new_dist_to_v = distances[u] + t
                if new_dist_to_v < distances[v]:
                    distances[v] = new_dist_to_v

        # check for negative cycles 
        for u, v, t in times:
            new_dist_to_v = distances[u] + t
            if new_dist_to_v < distances[v]:
                return None 

        max_dist = max(distances[1:])
        return max_dist if max_dist < float('inf') else -1
