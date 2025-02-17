class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = [0]*26
        for c in tiles:
            counter[ord(c)-ord("A")] += 1
        
        def seq_count(counter):
            tot = 1 # Empty string
            for opt in range(26):
                if counter[opt] != 0:
                    counter[opt] -= 1
                    tot += seq_count(counter)
                    counter[opt] += 1
            return tot
        
        return seq_count(counter) - 1
