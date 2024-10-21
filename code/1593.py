class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        best = 1

        def dfs(string, subs_set):
            nonlocal best
            n = len(subs_set)
            if string not in subs_set:
                best = max(best, n + 1)
            if len(string) == 0:
                return
            else:
                for i in range(1, len(string)):
                    if string[:i] not in subs_set:
                        new_set = copy.deepcopy(subs_set)
                        new_set.add(string[:i])
                        dfs(string[i:], new_set)
        dfs(s, set())
        return best
