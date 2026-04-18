from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj_list[from_i].append((to_i, price_i))

        q = deque([(src, 0)]) # node, total cost
        min_price = defaultdict(lambda: 1000)
        cnt = 0

        while q and cnt != k + 1:
            cnt += 1
            for _ in range(len(q)):
                node, total_cost = q.popleft()

                if node == dst:
                    min_price[dst] = min(min_price[dst], total_cost)

                for n, price in adj_list[node]:
                    new_cost = total_cost + price
                    if new_cost < min_price[n]:
                        min_price[n] = new_cost
                        q.append((n, new_cost))

        return min_price[dst] if min_price[dst] < 1000 else -1



        