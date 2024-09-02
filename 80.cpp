class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) {
            return n;
        }
        int i = 1;
        int j = 1;
        int k = 2;
        while (j < n - 1) {
            j++;
            if (nums[j] != nums[i-1]) {
                // We've found an element which hasn't occurred twice already
                i++;
                nums[i] = nums[j];
                k++;
            }
        }
        return k;        
    }
};
