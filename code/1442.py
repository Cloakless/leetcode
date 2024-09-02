class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        def xorVal(x,y):
            ans = arr[x]
            for p in range(x+1, y):
                ans ^= arr[p]
            return ans

        n = len(arr)
        tot = 0

        cache = [[-1 for x in range(n+1)] for y in range(n+1)]
        for i in range(n):
            for j in range(n+1):
                cache[i][j] = xorVal(i,j)

        for i in range(n-1):
            for j in range(i+1, n):
                for k in range(j, n):
                    if cache[i][j] == cache[j][k+1]:
                        tot += 1
        return tot
        
