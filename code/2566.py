class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        start1, start2, = None, None
        big, small = '', ''
        for c in num:
            if start1 is not None:
                if c == start1:
                    big += '9'
                else:
                    big += c
            else:
                if c != '9':
                    start1 = c
                big += '9'
                
            if start2 is not None:
                if c == start2:
                    small += '0'
                else:
                    small += c
            else:
                if c != '0':
                    start2 = c
                small += '0'
        return int(big) - int(small)
