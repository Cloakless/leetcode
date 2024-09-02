class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return 1;
        }
        int i = 0;
        int j = 0;
        int k = 1;
        while (j < n - 1) {
            j++;
            if (nums[j] != nums[j-1]) {
                // We've found a new element
                i++;
                nums[i] = nums[j];
                k++;
            }
        }
        return k;        
    }
};
