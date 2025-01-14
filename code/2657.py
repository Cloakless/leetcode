class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        counter = defaultdict(int)
        ans = []
        tot = 0
        for i in range(len(A)):
            counter[A[i]] += 1
            counter[B[i]] += 1
            if counter[A[i]] == 2:
                tot += 1
            if A[i] != B[i] and counter[B[i]] == 2:
                tot += 1
            ans.append(tot)
        return ans
