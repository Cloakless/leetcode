class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        neighs = defaultdict(list)
        for edge in edges:
            a, b = edge
            neighs[a].append(b)
            neighs[b].append(a)
        bob_path = []
        dfs_visited = {bob}
        def dfs(target, current):
            if target == current:
                bob_path.append(current)
                return True
            if len(neighs[current]) == 1 and neighs[current][0] in dfs_visited:
                return False
            for neigh in neighs[current]:
                if neigh not in dfs_visited:
                    dfs_visited.add(neigh)
                    cand = dfs(target, neigh)
                    if cand:
                        bob_path.append(current)
                        return True

        dfs(0, bob)
        bob_path = reversed(bob_path)
        bob_times = {}
        for i, val in enumerate(bob_path):
            bob_times[val] = i
        max_income = -1000000000000
        visited = {0}

        def bfs(current, income, step):
            nonlocal max_income
            step += 1
            if len(neighs[current]) == 1 and neighs[current][0] in visited:
                max_income = max(max_income, income)
                return None
            visited.add(current)
            for neigh in neighs[current]:
                if neigh not in visited:
                    visited.add(neigh)
                    if neigh not in bob_times or bob_times[neigh] > step:
                        bfs(neigh, income + amount[neigh], step)
                    elif bob_times[neigh] == step:
                        bfs(neigh, income + amount[neigh]//2, step)
                    else:
                        bfs(neigh, income, step)

        bfs(0, amount[0], 0)
        return max_income

        
