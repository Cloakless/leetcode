class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        freq_a, freq_b, freq_c = 0,0,0
        for char in s:
            if char == 'a':
                freq_a += 1
            elif char == 'b':
                freq_b += 1
            elif char == 'c':
                freq_c += 1
            else:
                assert "Unexpected character"
        if freq_a < k or freq_b < k or freq_c < k:
            return -1
        n = len(s)
        l = -1
        r = n
        freq_a, freq_b, freq_c = 0,0,0
        best = n
        while min(freq_a, freq_b, freq_c) < k:
            l += 1
            char = s[l]
            if char == 'a':
                freq_a += 1
            elif char == 'b':
                freq_b += 1
            elif char == 'c':
                freq_c += 1
            best = (n-r) + (l + 1)
        while l >= 0:
            l -= 1
            char = s[l+1]
            if char == 'a':
                freq_a -= 1
            elif char == 'b':
                freq_b -= 1
            elif char == 'c':
                freq_c -= 1
            while min(freq_a, freq_b, freq_c) < k:
                r -= 1
                char = s[r]
                if char == 'a':
                    freq_a += 1
                elif char == 'b':
                    freq_b += 1
                elif char == 'c':
                    freq_c += 1
            best = min(best, (n-r) + (l + 1))
        return best
        
