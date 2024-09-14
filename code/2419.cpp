class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int target = *max_element(nums.begin(), nums.end());
        int streak = 0;
        int best = 1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                streak++;
                best = max(best, streak);
            }
            else {
                streak = 0;
            }
        }
        return best;        
    }
};
