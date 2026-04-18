class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        start = points[0]

        visited = [False] * n
        total_cost = 0
        points_connected = 0

        heap = [(0, 0)]

        while heap:
            dist, i = heapq.heappop(heap)

            if visited[i]:
                continue

            visited[i] = True
            total_cost += dist
            points_connected += 1

            if points_connected == n:
                break

            curr_x, curr_y = points[i]

            for j in range(n):
                if not visited[j]:
                    next_x, next_y = points[j]
                    manhattan_dist = abs(curr_x - next_x) + abs(curr_y - next_y)
                    heapq.heappush(heap, (manhattan_dist, j))

        return total_cost
