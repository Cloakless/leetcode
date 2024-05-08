public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int removed = 0;
        int i = 1;
        int n = nums.Length;
        while (i < n) {
            if (nums[i] == nums[i-1]) {
                int j = i;
                while (j < n - 1) {
                    nums[j] = nums[j+1];
                    j++;
                }
                n--;
                i--;
            }
            i++;
        }
        return n;

    }
}
