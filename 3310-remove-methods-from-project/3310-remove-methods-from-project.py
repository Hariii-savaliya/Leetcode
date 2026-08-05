class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        
        adj = {i: [] for i in range(n)}
        for src, dst in invocations:
            adj[src].append(dst)

        que = [k]
        visited = set([k])
        while que:
            suspicious = que.pop()
            for neighbor in adj[suspicious]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    que.append(neighbor)
                    
        ans = []
        for method in range(n):
            if method in visited: continue
            for neighbor in adj[method]:
                if neighbor in visited:
                    return list(range(n))
            ans.append(method)
        return ans