class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int n = nums.size();
        vector<string> ans = {};
        if (n == 0) {
            return ans;
        }
        else if (n == 1) {
            ans.push_back(to_string(nums[0]));
            return ans;
        }
        int left = 0;
        int right = 0;
        int start;
        int end;
        while (right < n - 1) {
            // Two cases:
            // the next one is in the same range
            if (nums[right+1] == nums[right] + 1) {
                right++;
            }
            // the next one starts a new range
            else {
                // Save off the previous range
                // Either size == 1
                if (right - left == 0) {
                    start = nums[left];
                    ans.push_back(to_string(start));
                }
                // or size > 1
                else {
                    start = nums[left];
                    end = nums[right];
                    ans.push_back(to_string(start) + "->" + to_string(end));
                }
                left = right + 1;
                right = left;
            }
        }
        // Then we have the final range to add
        if (right - left == 0) {
            start = nums[left];
            ans.push_back(to_string(start));
        }
        // or size > 1
        else {
            start = nums[left];
            end = nums[right];
            ans.push_back(to_string(start) + "->" + to_string(end));
        }
        return ans;
    }
};
