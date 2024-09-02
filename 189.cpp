class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n; // Fully rotating multiple times is pointless
        vector<int> rot (nums.begin(), nums.begin() + n);
        for (int i = 0; i < n; i++) {
            rot[i] = nums[(i+(n-k)) % n];
        }
        for (int j = 0; j < n; j ++) {
            nums[j] = rot[j];
        }
    }
};
