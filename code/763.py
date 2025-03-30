class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = defaultdict(int)
        for i, c in enumerate(s):
            last_occurrence[c] = i
        start, end = 0,0
        ans = []
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                ans.append(i - start + 1)
                start = i+1
        return ans
