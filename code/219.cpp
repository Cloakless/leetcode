class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, vector<int>> indices;
        for (int i = 0; i < nums.size(); i++) {
            if (indices.contains(nums[i])) {
                vector<int> cands = indices[nums[i]];
                for (int j = 0; j < cands.size(); j++) {
                    if (abs(cands[j] - i) <= k) {
                        return true;
                    }
                }
                indices[nums[i]].push_back(i);
            }
            else {
                indices[nums[i]] = {i};
            }
        }
        return false;        
    }
};
