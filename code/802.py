class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        ans = []

        @cache
        def scan(x):
            if len(graph[x]) == 0:
                return True
            if x not in seen:
                seen.add(x)
                if len(graph[x]) == 0:
                    return True
                valid = True
                for y in graph[x]:
                    valid = (valid and scan(y))
                return valid                
            else:
                return False

        for i in range(n):
            seen = set()
            if not graph[i] or scan(i):
                ans.append(i)
        ans.sort()
        return ans
