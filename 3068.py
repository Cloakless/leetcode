class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        better = []
        worse = []
        for num in nums:
            alt = num^k
            if alt > num:
                better.append((alt-num,alt,num))
            else:
                worse.append((num-alt,alt,num))
        tot = 0
        if len(better) % 2 == 0:
            for (w,x,y) in better:
                tot += x
            for (w,x,y) in worse:
                tot += y
            return tot
        else:
            better.sort()
            worse.sort()
            for (w,x,y) in better:
                tot += x
            for (w,x,y) in worse:
                tot += y
            if len(worse) > 0 and better[0][0] > worse[0][0]:
                tot -= worse[0][0]
            else:
                tot -= better[0][0]
            return tot
        
