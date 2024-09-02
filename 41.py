class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        tog = True
        while tog:
            try:
                if nums[i] > 0:
                    tog = False
                i += 1
            except IndexError:
                return 1
        j = i - 1
        if j > len(nums):
            return 1
        place = j
        guess = 1
        if nums[j] > 1:
            return 1
        while True:
            tig = True
            while tig:
                try:
                    if nums[place] == nums[place+1]:
                        del nums[place+1]
                    else:
                        tig = False
                except IndexError:
                    tig = False
            try:
                if nums[place] != guess:
                    return nums[place-1] + 1
            except IndexError:
                return nums[place-1]+1
            place += 1
            guess += 1
