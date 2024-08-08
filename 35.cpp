class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 1) {
            if (nums[0] < target) {
                return 1;
            }
            else {
                return 0;
            }
        }
        int lower = 0;
        int upper = n;
        int mid;
        while (lower + 1 < upper) {
            mid = (lower + upper) / 2;
            if (nums[mid] < target) {
                lower = mid;
            }
            else {
                upper = mid;
            }
        }
        if (nums[lower] >= target) {
            // Either nums[lower] == target or it is the new start of the list
            return lower;
        }
        else {
            // It must be one more than lower, regardless of whether nums[upper] == target
            return upper;
        }
        
    }
};
