class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans = {0,0};
        unordered_map<int, int> index_map;
        for (int i = 0; i < nums.size(); i++) {
            if (index_map.count(target - nums[i])) {
                ans = {i, index_map[target - nums[i]]};
                return ans;
            }
            index_map[nums[i]] = i;
        }
        return ans;
    }
};
