class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        neighs, groups = defaultdict(set), [0]*n
        for a, b in edges:
            neighs[a-1].add(b-1)
            neighs[b-1].add(a-1)

        def is_bipartite(i):
            for neigh in neighs[i]:
                if groups[neigh] == groups[i]:
                    return False
                if groups[neigh] == 0:
                    groups[neigh] = 2 - ((groups[i] + 1) % 2)
                    if not is_bipartite(neigh):
                        return False
            return True

        # Sort into groups
        for i in range(n):
            if groups[i] == 0:
                groups[i] = 1
                if not is_bipartite(i):
                    return -1

        def max_path_length(start):
            nodes = set()
            nodes.add(start)
            visited = [False] * n
            visited[start] = True
            depth = 0
            while nodes:
                new_nodes = set()
                for curr_node in nodes:
                    for neigh in neighs[curr_node]:
                        if not visited[neigh]:
                            visited[neigh] = True
                            new_nodes.add(neigh)
                nodes = new_nodes
                depth += 1
            return depth

        distances, visited = [max_path_length(i) for i in range(n)], [False] * n

        def max_num_groups(node):
            ans = distances[node]
            visited[node] = True
            for neigh in neighs[node]:
                if not visited[neigh]:
                    ans = max(ans, max_num_groups(neigh))
            return ans
        
        ans = 0
        for node in range(n):
            if not visited[node]:
                ans += max_num_groups(node)
        return ans
