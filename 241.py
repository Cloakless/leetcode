class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        dp = [[None for _ in range(n)] for _ in range(n)]

        def operator(op):
            if op == '+':
                return lambda x, y: x + y
            elif op == '-':
                return lambda x, y: x - y
            else:
                return lambda x, y: x * y

        def calculate(i,j):
            if dp[i][j]:
                return dp[i][j]
            ans = []
            if (j - i) < 2:
                ans.append(int(expression[i:j+1]))
            else:
                for k in range(i+1,j):
                    if not expression[k].isdigit():
                        func = operator(expression[k])
                        l_ans = calculate(i, k-1)
                        r_ans = calculate(k+1, j)
                        for left in l_ans:
                            for right in r_ans:
                                ans.append(func(left, right))
            dp[i][j] = ans
            return ans
        return calculate(0, n-1)
