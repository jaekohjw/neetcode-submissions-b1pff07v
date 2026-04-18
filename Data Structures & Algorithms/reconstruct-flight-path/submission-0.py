class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for u, v in sorted(tickets):
            adj[u].append(v)

        res = []
        def dfs(airport):
            while adj[airport]:
                nei = adj[airport].pop(0)
                dfs(nei)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]
            

        