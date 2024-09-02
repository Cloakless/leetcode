class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        removed = 0
        digits = list(num)
        while removed < k:
            n = len(digits)
            if n == 0:
                return "0"
            elif n == 1:
                return "0"
            
            found_in_for = False
            for i in range(n-1):
                if int(digits[i]) > int(digits[i+1]):
                    digits.pop(i)
                    removed += 1
                    found_in_for = True
                    break
            if not found_in_for:
                # Lit is now monotonic
                digits = digits[0:n-k+removed]
                removed = k
        removing = True
        while removing:
            if len(digits) == 0:
                return "0"
            removing = False
            if digits[0] == "0":
                digits.pop(0)
                removing = True

        number = "".join(digits)
        if len(number) == 0:
            return "0"
        return number
        
