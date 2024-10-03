class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            sum %= p;
        }
        if (sum == 0) {
            return 0;
        }
        unordered_map<int, int> last_seen;
        last_seen[0] = -1;
        int acc = 0;
        int best = nums.size();
        for (int j = 0; j < nums.size(); j++) {
            acc += nums[j];
            acc %= p;
            int target = acc - sum + p;
            target %= p;
            if (last_seen.contains(target)) {
                best = min(best, j - last_seen[target]);
            }
            last_seen[acc] = j;
        }
        if (best == nums.size()) {
            return -1;
        }
        return best;
    }
};
