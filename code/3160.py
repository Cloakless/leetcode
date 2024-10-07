class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colours = defaultdict(int)
        counter = defaultdict(int)
        ans = []
        num_colours = 0
        for x, y in queries:
            if colours[x] != y:
                # White -> colour
                if counter[y] == 0:
                    num_colours += 1
                if colours[x] != 0:
                    prev = colours[x]
                    counter[prev] -= 1
                    if counter[prev] == 0:
                        num_colours -= 1
                colours[x] = y
                counter[y] += 1
            ans.append(num_colours)
        return ans
