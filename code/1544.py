class Solution:
    def makeGood(self, s: str) -> str:
        st = list(s)
        has = True
        l = len(st) + 1
        while len(st) < l:
            l = len(st)
            for i in range(len(st)):
                try:
                    if st[i].lower() == st[i+1].lower() and st[i] != st[i+1]:
                        del st[i+1]
                        del st[i]
                        has == True
                except IndexError:
                    pass
        if len(st) == 0:
            return ""
        else:
            return ''.join(st)       
