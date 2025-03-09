class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colours = colors # Couldn't be bothered to go back and change them
        idx = None
        n = len(colours)
        if colours[0] == colours[-1]:
            idx = 0
        else:
            for i in range(1, n):
                if colours[i-1] == colours[i]:
                    idx = i
        if idx is None:
            return n
        tot = 0
        streak = 1
        for i in range(idx, idx + n):
            if colours[i % n] == colours[(i-1) % n]:
                streak = 1
            else:
                streak += 1
            if streak >= k:
                tot += 1
        return tot



        
