class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        dominoes = [c for c in dominoes]
        n = len(dominoes)
        
        def next_interval(i):
            while True:
                if i >= n - 1:
                    return None, None
                elif dominoes[i+1] != '.':
                    i += 1
                else:
                    j = i + 1
                    while dominoes[j] == '.':
                        j += 1
                    return i, j
        
        left, right = next_interval(0)
        while left is not None:
            if dominoes[left] == dominoes[right]:
                for i in range(left+1, right):
                    dominoes[i] = dominoes[left]
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                pass
            else:
                length = right - left - 1
                for i in range(length//2):
                    dominoes[left+i+1] = dominoes[left]
                    dominoes[right-i-1] = dominoes[right]
            left, right = next_interval(right)
        ans = ''.join(dominoes)
        return ans[1:-1]


        
