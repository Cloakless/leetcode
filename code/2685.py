class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = defaultdict(set)
        comp_size = defaultdict(int)
        num_edges = defaultdict(int)
        for a, b in edges:
            neighbours[a].add(b)
            neighbours[b].add(a)

        component = [i for i in range(n)]
        comp_value = {}

        def canon(x):
            cand = x
            updates = [x]
            while component[cand] != cand:
                updates.append(cand)
                cand = component[cand]
            for update in updates:
                component[update] = cand
            return cand

        def connect(x, y):
            a, b = canon(x), canon(y)
            if a != b:
                component[a] = b

        for a, b in edges:
            connect(a, b)

        for i in range(n):
            comp_size[canon(i)] += 1

        for a, b in edges:
            num_edges[canon(a)] += 1
        ans = 0

        for comp in comp_size:
            if num_edges[comp] == comp_size[comp]*(comp_size[comp]-1)//2:
                ans += 1
        return ans
        
