class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        else if (n == 2) {
            if (nums[0] > nums[1]) {
                return nums[0];
            }
            else {
                return nums[1];
            }
        }
        int loot [n];
        loot[0] = nums[0];
        loot[1] = nums[1];
        for (int i = 2; i < n; i++) {
            if (i - 3 >= 0 && loot[i-3] > loot[i-2]) {
                loot[i] = nums[i] + loot[i-3];
            }
            else {
                loot[i] = nums[i] + loot[i-2];
            }
        }
        if (loot[n-1] > loot[n-2]) {
            return loot[n-1];
        }
        else {
            return loot[n-2];
        }
    }
};
