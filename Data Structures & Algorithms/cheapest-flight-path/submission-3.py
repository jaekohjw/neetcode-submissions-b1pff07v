from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj_list[from_i].append((to_i, price_i))

        q = deque([(src, 0)]) # node, total cost

        min_price = [float('inf')] * n
        min_price[src] = 0

        stops = 0

        while q and stops <= k:
            for _ in range(len(q)):
                node, total_cost = q.popleft()

                for neighbor, price in adj_list[node]:
                    new_cost = total_cost + price

                    if new_cost < min_price[neighbor]:
                        min_price[neighbor] = new_cost
                        if neighbor != dst:
                            q.append((neighbor, new_cost))
            
            stops += 1

        return min_price[dst] if min_price[dst] != float('inf') else -1



        