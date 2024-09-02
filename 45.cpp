class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int reachable[n];
        for (int i = 0; i < n; i++) {
            reachable[i] = 100000;
        }
        reachable[0] = 0;
        int cand;
        for (int j = 0; j < n; j++) {
            for (int jump = 1; j + jump < n && jump <= nums[j]; jump++) {
                cand = reachable[j] + 1;
                if (reachable[j + jump] > cand) {
                    reachable[j + jump] = cand;
                }
            }
        }
        return reachable[n-1];        
    }
};
