class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        start = points[0]

        visited = set()
        total_cost = 0

        heap = [(0, start)]

        def manhattan_dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        while heap:
            dist, curr_p = heapq.heappop(heap)

            if (curr_p[0], curr_p[1]) in visited:
                continue 

            total_cost += dist
            visited.add((curr_p[0], curr_p[1]))

            for p in points:
                if p != curr_p and (p[0], p[1]) not in visited:
                    heapq.heappush(heap, (manhattan_dist(curr_p, p), p))

        return total_cost
