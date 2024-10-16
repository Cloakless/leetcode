class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''
        k = 0
        while a + b + c > 0:
            if a >= b and a >= c:
                # Try to add a
                if (k < 2 or not (ans[k-1] == 'a' and ans[k-2] == 'a')):
                    ans += 'a'
                    a -= 1
                elif b >= c and b > 0:
                    ans += 'b'
                    b -= 1
                elif c > 0:
                    ans += 'c'
                    c -= 1
                else:
                    return ans
            elif b >= c:
                # Try to add b
                if (k < 2 or not (ans[k-1] == 'b' and ans[k-2] == 'b')):
                    ans += 'b'
                    b -= 1
                elif a >= c and a > 0:
                    ans += 'a'
                    a -= 1
                elif c > 0:
                    ans += 'c'
                    c -= 1
                else:
                    return ans
            elif c >= b and c >= a:
                # Try to add c
                if (k < 2 or not (ans[k-1] == 'c' and ans[k-2] == 'c')):
                    ans += 'c'
                    c -= 1
                elif b >= a and b > 0:
                    ans += 'b'
                    b -= 1
                elif a > 0:
                    ans += 'a'
                    a -= 1
                else:
                    return ans

            else:
                return ans
            k += 1
        return ans
