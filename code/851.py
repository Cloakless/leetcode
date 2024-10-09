class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        neighs = [[] for _ in range(n)]
        for rich, poor in richer:
            neighs[poor].append(rich)

        @lru_cache(maxsize=None)
        def quietest(person):
            if len(neighs[person]) == 0:
                return person
            best = person

            cands = neighs[person]
            for cand in cands:
                if quiet[quietest(cand)] < quiet[best]:
                    best = quietest(cand)
            return best

        return [quietest(person) for person in range(n)]
