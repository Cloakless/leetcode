class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Calculate distances
        dists = [[1000000 for _ in range(n)] for _ in range(n)]
        for x, y, weight in edges:
            dists[x][y] = weight
            dists[y][x] = weight
        for i in range(n):
            dists[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cand = dists[i][k] + dists[k][j]
                    if dists[i][j] > cand:
                        dists[i][j] = cand
                        dists[j][i] = cand

        def count_under(lst, m):
            tot = 0
            for elem in lst:
                if elem <= m:
                    tot += 1
            return tot

        city_dists = [count_under(dists[i], distanceThreshold) for i in range(n)]
        curr_min = n
        best_index = 0
        for p in range(n):
            if city_dists[p] <= curr_min:
                best_index = p
                curr_min = city_dists[p]
        return best_index
