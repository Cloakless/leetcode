class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        curr = 1
        counter = 1
        def nextNum(x):
            if x * 10 <= n:
                return x * 10
            elif (x + 1) % 10 == 0:
                x = x + 1
                while x % 10 == 0:
                    x //= 10
                return x
            elif (x + 1) > n:
                x = x // 10
                x += 1
                while x % 10 == 0:
                    x //= 10
                return x
            else:
                return x + 1
        while counter <= n:
            ans.append(curr)
            counter += 1
            curr = nextNum(curr)
        return ans
