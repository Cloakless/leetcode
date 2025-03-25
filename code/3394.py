class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        hs = []
        vs = []
        for a, b, c, d in rectangles:
            hs.append((a, 1))
            hs.append((c, -1))
            vs.append((b, 1))
            vs.append((d, -1))

        hs.sort()
        vs.sort()

        def cut_list(lst):
            zeros = set()
            zeros.add(0)
            num_overlap = 0
            for event, distance in lst:
                num_overlap += distance
                if num_overlap == 0:
                    zeros.add(event)
            return len(zeros) >= 4

        return cut_list(hs) or cut_list(vs)

        
