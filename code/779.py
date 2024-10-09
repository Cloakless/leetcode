class Solution:
    def kthGrammar(self, n: int, k: int) -> int:


        # 1234
        # 11223344

        # 5,6 -> 3

        def dfs(n, k):
            if k == 1:
                return 0
            if n == 1:
                return 0
            target = (k + 1) // 2
            prev = dfs(n-1, target)
            if prev == 0:
                if k % 2 == 0:
                    return 1
                else:
                    return 0
            else:
                if k % 2 == 0:
                    return 0
                else:
                    return 1

        return dfs(n, k)
