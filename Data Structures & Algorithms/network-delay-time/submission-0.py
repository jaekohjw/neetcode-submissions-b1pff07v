import heapq 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj_list[u].append((v, t))
        
        # Distance to all nodes starts as infinity
        distances = [float('inf') for _ in range(n + 1)]
        distances[k] = 0

        # min heap = (distance, node)
        heap = [(0, k)]

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            # skip if we have alr found a shorter path"
            if distances[curr_node] < curr_dist:
                continue 
            
            for neighbor, weight in adj_list[curr_node]:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        max_dist = 0
        for dist in distances[1:]:
            if dist == float('inf'):
                return -1 
            max_dist = max(max_dist, dist)

        return max_dist
            

        