class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        int i = 0;
        int j = n - 1;
        int k = 0;
        while (nums[j] == val) {
            j--;
            if (j < 0) {
                break;
            }
        }
        while (i <= j) {
            if (nums[i] != val) {
                k++;
                i++;
            }
            else {
                // Replace with one of the non-vals at the end of the array
                nums[i] = nums[j];
                j--;
                while (nums[j] == val) {
                    j--;
                    if (j < i) {
                        break;
                    }
                }
            }
        }
        return k;
    }
};
