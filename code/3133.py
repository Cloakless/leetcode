class Solution:
    def minEnd(self, n: int, x: int) -> int:
        x_bits = list(reversed(bin(n-1)[2:]))
        x_len = len(x_bits)
        n_bits = list(reversed(bin(x)[2:]))
        x_pos = 0
        for n_pos in range(len(n_bits)):
            if n_bits[n_pos] == '0':
                if x_pos < x_len:
                    n_bits[n_pos] = x_bits[x_pos]
                    x_pos += 1
                else:
                    break
        while x_pos < x_len:
            n_bits.append(x_bits[x_pos])
            x_pos += 1

        return int(''.join(n_bits[::-1]),2)
