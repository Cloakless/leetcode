class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tot = 0
        for num in nums:
            tot ^= num
        i = 1
        # print(tot)
        # return 0
        while True:
            print("i is {}".format(i))
            if tot & i != 0:
                break
            else:
                i = i << 1
        a = []
        b = []
        for num in nums:
            if (num & i) != 0:
                a.append(num)
            else:
                b.append(num)
        atot = 0
        btot = 0
        for aa in a:
            atot ^= aa
        for bb in b:
            btot ^= bb
        return [atot, btot]
    
