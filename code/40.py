class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def search(nums, target, path):
            for i in range(len(nums)):
                if nums[i] > target:
                    break
                elif i > 0 and nums[i] == nums[i-1]:
                    pass
                else:
                    new_path = path + [nums[i]]
                    if nums[i] == target:
                        ans.append(new_path)
                        break
                    else:

                        search(nums[i+1:], target - nums[i], new_path)
        search(candidates, target, [])
        return ans
