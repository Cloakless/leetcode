class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int median;
        // 0-indexed median
        if (n % 2 == 0) {
            median = n / 2 - 1;
        }
        else {
            median = (n + 1) / 2 - 1;
        }
        std::sort(nums.begin(), nums.begin() + n);
        return nums[median];        
    }
};
