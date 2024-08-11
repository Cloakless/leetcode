class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        bool reachable[n];
        for (int i = 0; i < n; i++) {
            reachable[i] = false;
        }
        reachable[0] = true;
        for (int j = 0; j < n; j++) {
            if (reachable[j]) {
                for (int jump = 1; j + jump < n && jump <= nums[j]; jump++) {
                    reachable[j + jump] = true;
                }
            }
        }
        return reachable[n-1];        
    }
};
