class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for u, v in sorted(tickets):
            adj[u].append(v)

        res = ["JFK"]
        def dfs(airport):
            if len(res) == len(tickets) + 1:
                return True
            if airport not in adj:
                return False
            
            tmp = list(adj[airport])
            for i, nei in enumerate(tmp):
                adj[airport].pop(i)
                res.append(nei)
                if dfs(nei): return True 
                adj[airport].insert(i, nei)
                res.pop()
            return False
        
        dfs("JFK")
        return res
            

        