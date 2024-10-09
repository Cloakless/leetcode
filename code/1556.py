class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = list(str(n))
        counter = 0
        ans = ''
        while s:
            if counter == 3:
                ans += '.'
                counter = 0
            ans += s.pop()
            counter += 1
        return ans[::-1]
        
