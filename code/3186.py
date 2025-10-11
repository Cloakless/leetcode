class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        power.sort()
        print(power)

        @cache
        def max_power(i):
            pointer = i
            while pointer < n and power[pointer] - power[i] <= 2:
                pointer += 1
            if pointer == n:
                j = i
                while j < n and power[i] == power[j]:
                    j += 1
                if j == n:
                    return sum(power[i:])
                else:
                    return max(sum(power[i:j]), max_power(j))
            j = i
            while power[j] == power[i]:
                j += 1
            return max(sum(power[i:j]) + max_power(pointer), max_power(j))
        return max_power(0)
        
