class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int lefts[n-1];
        int rights[n-1];
        lefts[0] = nums[0];
        rights[0] = nums[n-1];
        for (int i = 1; i < n - 1; i++) {
            lefts[i] = lefts[i-1] * nums[i];
            rights[i] = rights[i-1] * nums[n - i - 1];
        }
        nums[0] = rights[n-2];
        nums[n-1] = lefts[n-2];
        for (int j = 1; j < n - 1; j++) {
            nums[j] = lefts[j - 1] * rights[n - j - 2];
        }
        return nums;
    }
};
