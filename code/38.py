class Solution:
    def countAndSay(self, n: int) -> str:
        def next_num(s):
            ans = []
            curr = s[0]
            acc = 0
            for c in s:
                if c != curr:
                    ans.append(str(acc)+curr)
                    acc = 1
                    curr = c
                else:
                    acc += 1
            ans.append(str(acc)+curr)
            return ''.join(ans)
        ans = '1'
        for i in range(n-1):
            ans = next_num(ans)
        return ans
