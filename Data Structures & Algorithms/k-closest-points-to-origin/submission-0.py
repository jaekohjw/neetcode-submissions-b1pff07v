class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist_o(point):
            x = point[0]
            y = point[1]
            return math.sqrt(x ** 2 + y ** 2)

        points = [[dist_o(p), p] for p in points]
        heapq.heapify_max(points)
        while len(points) > k:
            heapq.heappop_max(points)
        
        return [p[1] for p in points]