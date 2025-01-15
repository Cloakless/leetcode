class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = bin(num2).count('1')
        target = bin(num1)[2::][::-1]
        ans = 0
        for i in reversed(range(len(target))):
            if n > 0 and target[i] == '1':
                ans += 2**i
                n -= 1
        j = 0
        while n > 0:
            if not (ans & 2**j):
                ans += 2**j
                n -= 1
            j += 1
        return ans

        
