class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        new_rungs = 0
        n = len(rungs)
        height = 0
        for rung in rungs:
            target = rung - height
            if target <= dist:
                height = max(height, rung)
            else:
                num_added = math.ceil((target - dist)  / dist)
                height += num_added * dist
                height = rung
                new_rungs += num_added
        return new_rungs
