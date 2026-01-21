class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        n = len(chars)
        def streak(i):
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            return j - i
        pointer, printer = 0,0
        while pointer < n:
            s = streak(pointer)
            c = chars[pointer]
            chars[printer] = c
            printer += 1
            ans += 1
            pointer += s
            if s > 1:
                string = list(str(s))
                for e in string:
                    chars[printer] = e
                    printer += 1
                    ans += 1
        return ans        
