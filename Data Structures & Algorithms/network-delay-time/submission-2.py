import heapq 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj_list[u].append((v, t))
        
        distances = [float('inf') for _ in range(n + 1)]
        distances[k] = 0

        heap = [(0, k)]
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            if curr_dist > distances[curr_node]:
                continue 

            for n, weight in adj_list[curr_node]:
                new_dist_to_n = curr_dist + weight
                if new_dist_to_n < distances[n]:
                    distances[n] = new_dist_to_n
                    heapq.heappush(heap, (new_dist_to_n, n))
        
        max_dist = max(distances[1:])
        return max_dist if max_dist < float('inf') else -1

