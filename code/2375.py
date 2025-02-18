class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [False] * 10
        n = len(pattern) + 1

        target = ''.join([str(i) for i in range(1,n+1)])
        cands = sorted([''.join(p) for p in permutations(target)])

        def match(cand, pattern):
            if len(cand) != len(pattern) + 1:
                return False
            for i in range(len(pattern)):
                if pattern[i] == 'I' and int(cand[i]) > int(cand[i+1]):
                    return False
                elif pattern[i] == 'D' and int(cand[i]) < int(cand[i+1]):
                    return False
            return True

        for cand in cands:
            if match(cand, pattern):
                return cand
        
