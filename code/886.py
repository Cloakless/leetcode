class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def process(person, parity):
            if person in group and group[person] != parity:
                return False
            else:
                group[person] = parity
                for other in dls[person]:
                    if other in group and group[other] != 1 - parity:
                        return False
                    if other not in group :
                        success = process(other, 1-parity)
                        if not success:
                            return False
            return True
            
        group = {}
        dls = defaultdict(set)
        for person in dislikes:
            dls[person[0]].add(person[1])
            dls[person[1]].add(person[0])

        for i in range(1, n+1):
            if i not in group:
                success = process(i, 0)
                if not success:
                    return False
        return True

        

        
