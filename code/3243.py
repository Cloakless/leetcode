class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = defaultdict(set)
        for i in range(n-1):
            edges[i].add(i+1)

        def bfs():
            neighs = set()
            neighs.add(0)
            dist = 0
            seen = set()
            while neighs:
                dist += 1
                new_set = set()
                for neigh in neighs:
                    for new_opt in edges[neigh]:
                        if new_opt == n - 1:
                            return dist
                        elif new_opt not in seen:
                            new_set.add(new_opt)
                            seen.add(new_opt)
                neighs = new_set
            return dist

        ans = []
        for u, v in queries:
            edges[u].add(v)
            ans.append(bfs())
        return ans
        
