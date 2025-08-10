class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power = 1
        powers = set()
        while power <= 10**9:
            powers.add(''.join(sorted(str(power))))
            power *= 2
        return ''.join(sorted(str(n))) in powers
