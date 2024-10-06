class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == 0:
            return 'b' * b
        elif b == 0:
            return 'a' * a
        ans = ''
        if b > a:
            b -= 1
            ans = 'b'
        else:
            a -= 1
            ans = 'a'
        if b > a:
            b -= 1
            ans += 'b'
        else:
            a -= 1
            ans += 'a'
        while a + b > 0:
            if b > a and not (ans[-1] == 'b' and ans[-2] == 'b'):
                ans += 'b'
                b -= 1
            elif not (ans[-1] == 'a' and ans[-2] == 'a'):
                ans += 'a'
                a -= 1
            else:
                ans += 'b'
                b -= 1
        return ans
       
