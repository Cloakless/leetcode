class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(profits, capital))
        projects.sort(key=lambda x: x[1])
        n = len(projects)
        if k > n:
            k = n
        while k > 0:
            if not projects:
                return w
            elif w < projects[0][1]:
                return w
            else:
                if w > projects[-1][1]:
                    projects.sort(key=lambda x: x[0])
                    for j in range(k):
                        w += projects[n-j-1][0]
                    return w
                best = projects[0][0]
                best_i = 0
                for i in range(n):
                    if projects[i][1] > w:
                        break
                    if projects[i][0] > best:
                        best_i = i
                        best = projects[i][0]
            projects.pop(best_i)
            w += best
            k -= 1
            n -= 1
        return w
