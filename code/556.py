class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        m = len(digits)
        doable = False
        for i in range(m-1):
            if digits[i] < digits[i+1]:
                doable = True
                break
        if not doable:
            return -1
        for j in reversed(range(m-1)):
            # Look at all digits to the right
            options = set(digits[j+1:])
            best = 10
            for option in options:
                if option > digits[j] and option < best:
                    best = option
            if best != 10:
                for k in reversed(range(j+1, m)):
                    if digits[k] == best:
                        digits[j], digits[k] = digits[k], digits[j]
                        digits = digits[:j+1] + sorted(digits[j+1:])
                        ans = int("".join(list(map(str, digits))))
                        return ans if ans < 2**31 else -1
        
