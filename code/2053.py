class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        sarr = defaultdict(int)
        for s in arr:
            sarr[s] += 1
        for t in arr:
            if sarr[t] == 1:
                count += 1
                if count == k:
                    return t
        return ""
