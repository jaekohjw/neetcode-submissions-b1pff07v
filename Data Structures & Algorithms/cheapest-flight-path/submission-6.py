class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj_list[from_i].append((to_i, price_i))

        # (cost, node, stops used)
        heap = [(0, src, 0)] 
        # visisted[node] = min stops used to reach it at any cost
        visited = {} 

        while heap: 

            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops > k:
                continue

            if node in visited and visited[node] <= stops:
                continue

            visited[node] = stops

            for nei, price in adj_list[node]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1





        