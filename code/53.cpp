class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int best = nums[0];
        int worst = 0;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            best = max(best, sum - worst);
            worst = min(worst, sum);
        }
        return best;   
    }
};
