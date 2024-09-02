class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return (nums[0] >= target);
        }
        int tot = 0;
        int left = 0;
        int right = -1;
        int best = -1;
        while (tot < target) {
            right++;
            if (right == n) {
                return 0;
            }
            tot += nums[right];
        }
        best = right - left + 1;
        while (right < n) {
            while (tot >= target) {
                best = min(best, right - left + 1);
                tot -= nums[left];
                left++;
                if (left > right) {
                    right = left;
                    tot = nums[left];
                }
            }
            while (tot < target) {
                right++;
                if (right >= n) {
                    return best;
                }
                tot += nums[right];
            }
        }
        return best;
    }
};
