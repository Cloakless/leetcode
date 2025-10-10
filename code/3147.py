class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        @cache
        def get_energy(i):
            if i + k >= n:
                return energy[i]
            else:
                return energy[i] + get_energy(i+k)
        
        return max([get_energy(i) for i in range(n)])
