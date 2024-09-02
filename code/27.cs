public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int changed = 0;
        int i = 0;
        int n = nums.Length;
        while (i < n) {
            while (n > 0 && nums[n-1] == val) {
                n--;
            }
            if (i >= n) {
                break;
            }
            if (nums[i] == val) {
                changed++;
                int a = nums[i];
                int b = nums[n-1];
                nums[i] = b;
                nums[n-1] = a;
            }
            i++;
        }
        return n;

    }
}
